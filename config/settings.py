import sys,os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DATABASE = dict(dbpath=os.path.join(BASE_DIR,'database'),tables={'users':"userphone",'userstoken':"userstoken","Liaison":"liaison"},)

#日志目录
LOG_PATH = os.path.join(BASE_DIR,'logs')


URL      = "http://192.168.10.32:808"


CODE     = "8888"

#发送验证码验证类型 1登录,2忘记密码

SEND_CODE=1


