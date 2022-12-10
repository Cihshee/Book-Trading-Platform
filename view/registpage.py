import tkinter
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from view.view import *  # 菜单栏对应的各个子页面
from view.mainpage import MainPage
import view.login as login

class RegistPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("500x500")
        self.root.title('注册')
        self.stuno = StringVar()
        self.stuname = StringVar()
        self.sex = StringVar()
        self.phoneno = StringVar()
        self.passwordone = StringVar()
        self.passwordtwo = StringVar()
        self.page = Frame(self.root)  # 创建Frame
        self.createPage()

    def createPage(self):
        self.page.pack()
        ttk.Label(self.page, text="校园二手书交易平台", font='SimSun 25 bold').grid(row=0, stick=W + E, pady=40, columnspan=2)
        ttk.Label(self.page, text='学    号: ', font='SimSun -14').grid(row=1, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.stuno).grid(row=1, column=1, sticky=W)
        ttk.Label(self.page, text='姓    名: ', font='SimSun -14').grid(row=2, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.stuname).grid(row=2, column=1, sticky=W)
        ttk.Label(self.page, text='性    别: ', font='SimSun -14').grid(row=3, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.sex).grid(row=3, column=1, sticky=W)
        ttk.Label(self.page, text='电    话: ', font='SimSun -14').grid(row=4, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.phoneno).grid(row=4, column=1, sticky=W)
        ttk.Label(self.page, text='密    码: ', font='SimSun -14').grid(row=5, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.passwordone, show='*').grid(row=5, column=1, sticky=W)
        ttk.Label(self.page, text='确认密码: ', font='SimSun -14').grid(row=6, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.passwordtwo, show='*').grid(row=6, column=1, sticky=W)
        ttk.Button(self.page, text='提 交', width=30, command=self.regist, bootstyle="primary-outline").grid(row=7,column=0,columnspan=2,pady=20)
        #ttk.Button(self.page, text='返 回', width=30, command=self.back, bootstyle="primary-outline").grid(row=8, column=0, columnspan=2)


    def regist(self):
        one = self.passwordone.get()
        two = self.passwordtwo.get()
        if one != two:
            showinfo(title='提示', message='两次输入的密码不一致！')
        else:

            showinfo(title='提示', message='注册成功！')
            self.page.destroy()
            MainPage(self.root)