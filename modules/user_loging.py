
import os,random


from config import  settings
from  dbhelper import dbapi
from modules import common


class CommonalityUserMethod(object):
    '''公共类实现,用户登录，保存登录后token,修改密码等操作'''
    _database   = "{0}.db".format(os.path.join(settings.DATABASE['dbpath'],settings.DATABASE['tables']['users']))#userphone
    _database_1 = "{0}.db".format(os.path.join(settings.DATABASE['dbpath'],settings.DATABASE['tables']['userstoken']))
    def __init__(self):
        self.dict_user = self.get_load_user()#读取用户信息然后保存到self.dict_user中
        self.username  = list(self.dict_user.keys())[0]
        self.updat_random_password = self.random_password()


    def get_load_user(self):
           return dbapi.load_data_from_db(self._database)


    def get_load_usertoken(self):
          self.dic_user_token = dbapi.load_data_from_db(self._database_1)
          return self.dic_user_token


    def write_clear_user_token(self,content):
        '''登录成功后保存token到本地，退出成功后清除本地token'''
        dbapi.write_db_json(content,self._database_1)


    def write_user_update_password(self,content):
        '''重置用户密码，更新到用户表'''
        dbapi.write_db_json(content,self._database)


    def updata_user(self):
        '''用户数据更新'''
        try:
            dbapi.write_db_json(self.dict_user,self._database)
            return True
        except Exception as e:
            common.write_log("用户登录页面更新用户数据:{0}".format(e))
            return False


    def undata_newiphone(self,newargs):
        '''修改更新密码'''
        self.dict_user[self.username]['password'] = newargs
        result  = self.updata_user()
        if result:
            print("更新密码成功")
            return True
        else:
            print("更新密码失败，请检查数据")
            return False


    def random_password(self):
        '''生成随机密码'''
        checkcode = ""
        for i in range(6):
            tem = random.randint(1,6)
            checkcode += str(tem)
        checkcode ="{0}t".format(checkcode)
        return checkcode





if __name__ == '__main__':
    obj = CommonalityUserMethod()
    obj.random_password()








