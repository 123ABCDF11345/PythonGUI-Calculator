import tkinter
import time
import threading
 
class choujiang:
    #初始化魔术方法
    def __init__(self):
        #准备好界面
        self.root = tkinter.Tk()
        self.root.title('抽学号  汪俊择')
        self.root.minsize(300, 300)
        # 声明一个是否按下开始的变量
        self.isloop = False
        self.newloop = False
        #调用设置界面的方法
        self.setwindow()
        self.root.mainloop()
 
 
 
    #界面布局方法
    def setwindow(self):
        #开始停止按钮
        self.btn_start = tkinter.Button(self.root, text = 'start/stop',command = self.newtask)
        self.btn_start.place(x=90, y=125, width=50, height=50)
 
        self.btn1 = tkinter.Button(self.root, text='1', bg='red')
        self.btn1.place(x=20, y=20, width=50, height=50)
 
        self.btn2 = tkinter.Button(self.root, text='2', bg='white')
        self.btn2.place(x=90, y=20, width=50, height=50)
 
        self.btn3 = tkinter.Button(self.root, text='3', bg='white')
        self.btn3.place(x=160, y=20, width=50, height=50)
 
        self.btn4 = tkinter.Button(self.root, text='4', bg='white')
        self.btn4.place(x=230, y=20, width=50, height=50)
 
        self.btn5 = tkinter.Button(self.root, text='5', bg='white')
        self.btn5.place(x=230, y=90, width=50, height=50)
 
        self.btn6 = tkinter.Button(self.root, text='6', bg='white')
        self.btn6.place(x=230, y=160, width=50, height=50)
 
        self.btn7 = tkinter.Button(self.root, text='7', bg='white')
        self.btn7.place(x=230, y=230, width=50, height=50)
 
        self.btn8 = tkinter.Button(self.root, text='8', bg='white')
        self.btn8.place(x=160, y=230, width=50, height=50)
 
        self.btn9 = tkinter.Button(self.root, text='9', bg='white')
        self.btn9.place(x=90, y=230, width=50, height=50)
 
        self.btn10 = tkinter.Button(self.root, text='3', bg='white')
        self.btn10.place(x=20, y=230, width=50, height=50)
 
        self.btn11 = tkinter.Button(self.root, text='2', bg='white')
        self.btn11.place(x=20, y=160, width=50, height=50)
 
        self.btn12 = tkinter.Button(self.root, text='1', bg='white')
        self.btn12.place(x=20, y=90, width=50, height=50)
 
        # 将所有选项组成列表
        self.girlfrends = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12]
 
    def rounds(self):
        # 判断是否开始循环
        if self.isloop == True:
            return
 
        # 初始化计数  变量
        i = 0
        # 死循环
        while True:
            if self.newloop == True:
                self.newloop = False
                return
 
            # 延时操作
            time.sleep(0.1)
            # 将所有的组件背景变为白色
            for x in self.girlfrends:
                x['bg'] = 'white'
 
            # 将当前数值对应的组件变色
            self.girlfrends[i]['bg'] = 'red'
            # 变量+1
            i += 1
            # 如果i大于最大索引直接归零
            if i >= len(self.girlfrends):
                i = 0
 
    # 建立一个新线程的函数
    def newtask(self):
        if self.isloop == False:
            # 建立线程
            t = threading.Thread(target = self.rounds)
            # 开启线程运行
            t.start()
            # 设置循环开始标志
            self.isloop = True
        elif self.isloop == True:
            self.isloop = False
            self.newloop = True
 
 
 
c = choujiang()
