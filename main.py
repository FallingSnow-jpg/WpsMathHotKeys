import tkinter
import keyboard
import pymouse

tk=tkinter.Tk()
mouse = pymouse.PyMouse()
readme="""数学公式快捷键程序依靠此窗口运行

ctrl+shift+y进入公式界面
ctrl+shift+u点击分数
ctrl+shift+n点击上下标
ctrl+shift+m点击根式
"""
tk.geometry("200x170")
lab=tkinter.Label(tk,text=readme)

lab.pack()

#以下内容在全屏情况下在wps-插入界面使用
keyboard.add_hotkey('ctrl+alt+y',mouse.click,args=(1270,85,1))#ctrl+shift+y进入公式界面
#以下内容在全屏情况下在wps-插入-公式界面使用
keyboard.add_hotkey('ctrl+alt+u',mouse.click,args=(670,85,1))#ctrl+shift+u点击分数
keyboard.add_hotkey('ctrl+alt+n',mouse.click,args=(720,85,1))#ctrl+shift+n点击上下标
keyboard.add_hotkey('ctrl+alt+m',mouse.click,args=(780,85,1))#ctrl+shift+m点击根式

tk.mainloop()

