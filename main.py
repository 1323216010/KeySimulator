import json
import win32gui
import win32con
import time
from pynput.keyboard import Controller, Key

def set_foreground_window(name):
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        # 没有找到窗口
        print(f'没有找到名为"{name}"的窗口。')
        return
    win32gui.ShowWindow(handle, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(handle)

keyboard = Controller()

set_foreground_window('test.txt - Notepad')  # 将记事本设为活动窗口
time.sleep(1)  # 等待一秒，确保窗口已经激活

# 读取并解析keys.json文件
with open('keys.json', 'r') as f:
    data = json.load(f)

# 遍历对象列表
for obj in data['keys']:
    # 模拟按键
    for key in obj['key']:
        keyboard.press(key)

    # 延迟指定的时间
    time.sleep(obj['time'])

    for key in obj['key']:
        keyboard.release(key)
#

# from utils import print_window_title
# win32gui.EnumWindows(print_window_title, None)

# from pynput.keyboard import Controller
# from pynput.keyboard import Key
# import time
# # 模拟输入特殊按键
#
# keyboard = Controller()
#
# # 模拟组合键
# keyboard.press('a')
# keyboard.release('a')
# keyboard.press(Key.space)
# keyboard.release(Key.space)
#
# # 模拟长按键
# keyboard.press('a')
# time.sleep(1)
# keyboard.release('a')
