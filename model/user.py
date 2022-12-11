# -*- coding: utf-8 -*-
"""
@Time: 2022/4/27 20:10 
@Author: Marigold
@Version: 0.0.0
@Description：
@WeChat Account: Marigold
"""


class User(object):
    def __init__(self, studentNo, studentName, sex, phoneNumber, address, studentKey):
        super(User, self).__init__()
        self.studentNo = studentNo
        self.studentName = studentName
        self.sex = sex
        self.phoneNumber = phoneNumber
        self.address = address
        self.studentKey = studentKey


    def get_studentNo(self):
        return self.studentNo

    def set_(self, studentNo):
        self.studentNo = studentNo
        return True




    # def get_user_id(self):
    #     return self.user_id
    #
    # def set_user_id(self, user_id):
    #     self.user_id = user_id
    #     return True
    #
    # def get_username(self):
    #     return self.username
    #
    # def set_username(self, username):
    #     self.username = username
    #     return True
    #
    # def get_password(self):
    #     return self.password
    #
    # def set_password(self, pwd):
    #     self.password = pwd
    #     return True
    #
    # def get_is_deleted(self):
    #     return self.is_deleted
    #
    # def set_is_deleted(self, is_deleted):
    #     self.is_deleted = is_deleted
    #     return True
