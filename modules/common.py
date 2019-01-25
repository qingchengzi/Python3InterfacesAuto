import time,os,random
from datetime import  datetime
from config   import  settings
import hashlib


def write_log(conetent):
    """
    将错误信息写入到日志
    :param conetent:
    :return:
    """
    _content  ="\n{0}:{1}".format(datetime.now().strftime("%Y-%m-%d %X"),conetent)
    _filename = os.path.join(settings.LOG_PATH,"errrlog.log")
    with open(_filename,'a+') as fa:
        fa.write(_content)

def Md5_Encrypting(newPwd):
    '''对密码进行加密'''
    newPwd_reversal = newPwd[::-1]  #加密算法
    obj             = hashlib.md5(bytes("{0}{1}".format(newPwd,newPwd_reversal),encoding='utf-8'))
    md5_Password    = obj.hexdigest()
    return md5_Password

def random_iphone_no():#生成数据手机号
    prelist   =["130","131","132","133","134","135","136","137","138","139","147","150","151",
                "152","153","155","156","157","158","159","186","187","188"]
    iphone_no =random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
    return iphone_no



