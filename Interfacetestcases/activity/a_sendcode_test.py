
import unittest,os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from handle.login_handle import LoginHandle
from modules.user_loging import CommonalityUserMethod



class  SendCode(unittest.TestCase):
       '''发送验证码 例子'''
       @classmethod
       def setUpClass(cls):
           cls.log_obj  = LoginHandle()
           cls.user_obj = CommonalityUserMethod()
           cls.phone    = cls.user_obj.dict_user[cls.user_obj.username]['phone']#读取用户手机号码

       #例子
       def test_01_get_colde_phone_null(self):
           '''手机号码为空获取验证码'''
           rest = self.log_obj.get_sendcode()
           self.assertTrue(rest)


       def test_03_mycenter(self):
           '''携带登录成功后的token访问个人中心'''
           rest = self.log_obj.intocentent()
           self.assertTrue(rest)


       def test_03_resetpwd(self):
           '''重置密码'''
           rest = self.log_obj.resetpwd()
           self.assertTrue(rest)


       @classmethod
       def tearDownClass(cls):
           pass



if __name__ == '__main__':

      unittest.main()
