该接口框架适用于HTTP协议的Web接口自动化测试；

基于Python3+Request+Unittest+HTMLTestRunner编写的接口自动化框架；

main_run.py入口文件、执行完毕后通过send_email.py发送测试结果到设定邮箱；

Interfacetestcases目录用于编写测试用例，可根据需求继续划分目录;

config目录>>settings.py是配置文件，用于定义常量；
database>>>目录是数据目录，将需要保存的数据保存到该目录下面，数据可以是（文本，数据库，文件）等等；
          例子中：使用文本的形式保存用户登录账号、密码、手机号码和用户登录成功后的cookies等信息;

dbhelper目录>>dbapi.py文件通过modules目录中的.py调用dbapi.py文件，完成对database目录中数据的增删改查操作；

handle目录>>login_handle.py文件测试用例和获取到的数值进行逻辑判断，将判断结果返回到测试用例中进行断言,根据需要自定义多个handle.py文件;

logs日志目录;

modules目录>定义的都是公共文件，例如：common.py定义了写入日志，生成手机号码，加密等函数；user_loging.py中定义了登录成功后将Token保存到
本地文件，方便后面需要携带Token访问的请求调用，以及修改密码，更新密码等功能；

report测试报告目录;

执行流程
在Interfacetestcses目录中定义测试用例，用例中逻辑在handle目录下面.py文件里面写类进行逻辑判断，需要调用公共数据的通过在modules目录中定义具体的函数进行调用
