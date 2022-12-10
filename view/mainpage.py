import tkinter
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from view.view import *  # 菜单栏对应的各个子页面
import view.login as login

class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("1000x600")
        # f = open('user.txt', 'r', encoding='utf-8')
        # self.tablename = f.read()
        # f.close()
        self.root.title('校园二手书交易平台欢迎您！')
        # self.root.resizable(0, 0)
        self.createPage()

    def createPage(self):
        #创建不同Frame
        self.Add = AddFrame(self.root)  #上传书籍
        self.Search = SearchFrame(self.root)    #查询书籍
        self.Quest = QuestFrame(self.root)  #收购帖
        self.List = ListFrame(self.root)    #我的订单
        self.Edit = EditFrame(self.root)    #个人信息
        # self.Editinfo = EditFrame(self.root)
        # self.Delete = DeleteFrame(self.root)

        self.Search.grid()  # 默认显示查询界面
        menubar = Menu(self.root)
        menubar.add_command(label='查询书籍', command=self.search, font='SimSun -14')
        menubar.add_command(label='上传书籍', command=self.add, font='SimSun -14')
        # menubar.add_command(label='更新', command=self.edit, font='SimSun -14')
        # menubar.add_command(label='删除', command=self.delete, font='SimSun -14')
        # menubar.add_command(label='备份与恢复', command=self.copy, font='SimSun -14')
        menubar.add_command(label='图书收购帖', command=self.quest, font='SimSun -14')
        menubar.add_command(label='我的订单', command=self.list, font='SimSun -14')
        menubar.add_command(label='修改信息', command=self.edit, font='SimSun -14')
        menubar.add_command(label='退出账户', command=self.out, font='SimSun -14')
        self.root['menu'] = menubar  # 设置菜单栏

    def add(self):
        self.Add.grid()
        self.Search.grid_forget()
        self.Quest.grid_forget()
        self.List.grid_forget()
        self.Edit.grid_forget()

    def search(self):
        self.Add.grid_forget()
        self.Search.grid()
        self.Quest.grid_forget()
        self.List.grid_forget()
        self.Edit.grid_forget()

    def quest(self):
        self.Add.grid_forget()
        self.Search.grid_forget()
        self.Quest.grid()
        self.List.grid_forget()
        self.Edit.grid_forget()

    def list(self):
        self.Add.grid_forget()
        self.Search.grid_forget()
        self.Quest.grid_forget()
        self.List.grid()
        self.Edit.grid_forget()

    def edit(self):
        self.Add.grid_forget()
        self.Search.grid_forget()
        self.Quest.grid_forget()
        self.List.grid_forget()
        self.Edit.grid()

    def out(self):
        if askokcancel('提示', '确定要切换账户？'):
            self.root.destroy()
            root = tkinter.Tk()
            root.title("校园二手书交易平台")
            login.LoginPage(root)
            root.mainloop()
