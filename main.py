import keyboard
import pymouse

mouse = pymouse.PyMouse()

#以下内容在全屏情况下在wps-插入界面使用
keyboard.add_hotkey('ctrl+alt+y',mouse.click,args=(1270,85,1))#ctrl+shift+y进入公式界面
#以下内容在全屏情况下在wps-插入-公式界面使用
keyboard.add_hotkey('ctrl+alt+u',mouse.click,args=(670,85,1))#ctrl+shift+u点击分数
keyboard.add_hotkey('ctrl+alt+n',mouse.click,args=(720,85,1))#ctrl+shift+n点击上下标
keyboard.add_hotkey('ctrl+alt+m',mouse.click,args=(780,85,1))#ctrl+shift

keyboard.wait()
