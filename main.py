import threading
import time
import tkinter
from tkinter import *
from sqlInteract import sqlI
from tkinter import scrolledtext
from pyspark import SparkConf,SparkContext
from tkinter import messagebox
# import os
# os.environ['PYTHON_PATH']=r'E:\programme\Python\Pylearn\GUI\example\DrawingBoard'
from tkinter.messagebox import showinfo
loginsuccess=False
from configmodel import config

class Main():
    def __init__(self,master):
        self.master=master
        renderMain_thread = threading.Thread(target=self.renderMain)
        renderMain_thread.start()
    def renderMain(self):
        global loginsuccess
        while loginsuccess!=True:
            time.sleep(0.1)
        main_page=ManagePage(self.master)
        main_page.place(x=0,y=0,relheight=1,relwidth=1)
class ManagePage(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.sqlI=sqlI
        self.creatWidget()
        self.init_Page()

    def creatWidget(self):
        # showArea
        self.showArea=Listbox(self,bg=config.get_color(),exportselection=True,
                              selectmode=MULTIPLE)
        self.showArea.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.7)
        vbar=Scrollbar(self,orient=VERTICAL,bg=config.get_color())
        self.showArea.config(yscrollcommand=vbar.set)
        vbar.config(command=self.showArea.yview)
        # entry
        Label(self,text='username').place(relx=0.25,rely=0.75)
        self.na_inp=Entry(self)
        self.na_inp.place(relx=0.4,rely=0.75)
        Label(self,text='password').place(relx=0.25,rely=0.8)
        self.pw_inp=Entry(self)
        self.pw_inp.place(relx=0.4,rely=0.8)
        # button
        self.checka_all=Button(self,text='check all')
        self.checka_all.place(relx=0.3,rely=0.9)
        self.checka_all.bind('<Button-1>',self.check_allE)

        self.insert=Button(self,text='insert')
        self.insert.place(relx=0.5,rely=0.90)
        self.insert.bind('<Button-1>',self.insertuser)

        self.delete_button = Button(self, text='delete')
        self.delete_button.place(relx=0.7,rely=0.90)
        self.delete_button.bind('<Button-1>', self.delete)

    def delete(self, e):
        selindex:tuple=self.showArea.curselection()
        for index in selindex:
            selText:str=self.showArea.get(index)
            info_list:list=selText.strip('\n').split(' ')
            print(info_list)
            print(self.sqlI.delUser(int(info_list[0]),info_list[1],info_list[2]))
        self.showcontentvialist()
    def insertuser(self,e):
        username=self.na_inp.get()
        pw=self.pw_inp.get()
        self.sqlI.insertUser(1,username,pw)
        self.showcontentvialist()
    def check_all(self):
        self.showArea.delete(1.0, END)
        res = self.sqlI.getUser()
        self.showArea.insert(1.0, f'id\tusername\tpassword\n')
        for ele in res:
            self.showArea.insert(1.0, f'{ele[0]}\t{ele[1]}\t{ele[2]}\n')

    def showcontentvialist(self):
        res = self.sqlI.getUser()
        self.showArea.insert(END, f'id username password\n')
        for ele in res:
            self.showArea.insert(END, f'{ele[0]} {ele[1]} {ele[2]}\n')

    def check_allE(self,e):
        self.showcontentvialist()
    def init_Page(self):
        self.showcontentvialist()

class LoginPage(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.creatWidget()
    def creatWidget(self):
        # input
        Label(self,text='username').grid(row=0,column=0,pady=5)
        self.usNaInput=Entry(self)
        self.usNaInput.grid(row=0,column=1)
        self.usNaInput.insert(0,'zjl')
        Label(self, text='password').grid(row=1, column=0,pady=10)
        self.usPaInput=Entry(self,show='*')
        self.usPaInput.grid(row=1,column=1)
        self.usPaInput.insert(0,'123')
        # button
        self.log_button=Button(self,text='log in')
        self.log_button.grid(row=2,column=0)
        self.log_button.bind('<Button-1>',self.login)

        self.sign_button=Button(self,text='sign up')
        self.sign_button.grid(row=2,column=1)
        self.sign_button.bind('<Button-1>',self.signUp)

    def signUp(self,e:tkinter.Event):
        pass
        # self.destroy()
    def login(self,e):
        un = self.usNaInput.get()
        pw = self.usPaInput.get()
        res = sqlI.checkSignPassword(un, pw)
        if res != 0:
            # showinfo('hint', message='login successfully')
            self.destroy()
        else:
            showinfo('hint', message='failes to login')
        global loginsuccess
        loginsuccess=True

if __name__=='__main__':
    root=Tk(className='passwordManager')
    root.geometry('500x500+500+200')
    loginP=LoginPage(root)
    loginP.pack()
    main=Main(root)
    # main_page=MainPage(root)
    # main_page.place(x=0,y=0,relheight=1,relwidth=1)
    root.mainloop()