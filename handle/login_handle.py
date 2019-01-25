#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/8/29 17:11'

import requests
from config import settings
from modules.user_loging import CommonalityUserMethod

class LoginHandle:

    def __init__(self):
        self.url      = settings.URL
        self.user_obj = CommonalityUserMethod()
        self.phone    = self.user_obj.dict_user[self.user_obj.username]['phone']#读取用户手机号码
        self.login_sucess()


    def get_token(self):
        """获取用户登录后的token"""
        return  self.user_obj.get_load_usertoken()['Obj']['Token']


    def get_sendcode(self):
        '''例子伪代码,手机号码为空type也为空'''
        url = "{0}{1}".format(self.url,"/Member/SendCode")
        payload = {
            "phone":"",
            "type" :"",
        }

        rest = requests.post(url=url,data=payload).json()

        if rest['Msg']=="手机号码不正确":
            return True
        else:
            return False


    def login_sucess(self):
        """获取登录成功后的cookies且保存到本地伪代码"""
        url = "{0}{1}".format(self.url,"/Member/Login")
        payload = {
            "phone":self.phone,
            "code" :"xx",
            "loginModel":"xooo",
            "rid" : ""
        }
        rest = requests.post(url,data=payload).json()
        if rest["Code"]==0:
            self.user_obj.write_clear_user_token(rest)



    def resetpwd(self):
        """伪代码修改密码后更新密码"""
        url = "{0}{1}".format(self.url,"/Member/ReSetPwd")
        payload ={
            "phone":self.phone,
             "pwd" :self.user_obj.updat_random_password,
        }
        rest = requests.post(url,data=payload).json()
        if rest["Code"]==0:
           return self.user_obj.undata_newiphone(self.user_obj.updat_random_password)
        else:
            print("修改密码错误")
            return False


    def intocentent(self,*args,**kwargs):
        '''携带token进入个人中心'''
        token = self.get_token()
        url   = "{0}{1}".format(self.url,"/Member/centent")
        header={
            "x-token":token
        }
        rest = requests.post(url=url,header=header).json()
        if rest["Msg"]=="个人中心":
            return True
        else:
            return False


    def logout(self,*args,**kwargs):
        '''退出登录'''
        url = "{0}{1}".format(self.url,"/Member/Logout")





