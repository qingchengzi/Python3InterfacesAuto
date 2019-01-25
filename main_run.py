

import time,unittest

from HTMLTestRunner import HTMLTestRunner

import send_email



def createst():
    '''执行Interface_test_cases目录已._test.py结尾的py文件'''
    test_dir = "./Interfacetestcases"
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')#将测试目录下已_test.py结尾py文件中测试用例全部放到列表中
    return discover  #返回unittest.suie.TestSuite类

if __name__ == '__main__':

    now        = time.strftime("%Y-%m-%d %H_%M_%S") #根据执行测试用例时间，生成测试报告名称
    title_str  = time.strftime("%Y-%m-%d %H:%M")    #根据测试用执行时间，生成测试报告内标题的时间
    filename   = "{0}{1}{2}".format('./report/',now,'_result.html')#测试报告目录和名称
    with open(filename,'wb') as write:  #将执行结果写入到HTMLTestRunner中
        runner = HTMLTestRunner(stream= write,  #with opne打开的文件句柄，必填项
                                title ='{0}xxooo自动化测试报告'.format(title_str),#测试报告中自定义标题名称，该参数为选填项
                                description='运行环境内测') #描述 ，该参数为选填项

        runner.run(createst())  #执行测试用例且生成.html测试报告

    send_email.main_email()    #测试用例执行完毕后，调用发邮件方法，发送邮件；

