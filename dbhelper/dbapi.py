
from config import settings
from modules.common import  write_log
import json

def load_data_from_db(tablename):
    '''读取会员信息'''
    try:
        with open(tablename,'r+',encoding='utf-8') as fr:
            return json.load(fr)
    except Exception as e:
        write_log(e)


def write_db_json(content,filename):
    try:
        with open(filename,'w+') as fw:
            fw.write(json.dumps(content))
    except Exception as e:
        write_log("dbapi方法中更新用户信息:{0}".format(e))


