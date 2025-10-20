from idlelib.configdialog import KeysPage
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
wd = webdriver.Edge()
wd.implicitly_wait(3)
wd.get("http://www.unixde.com/")
ac = ActionChains(wd)

ac.pause()

ele1 = w

# # 悬停
# ac.move_to_element()
#
# # 按住左键不放
# ac.click_and_hold()
#
# # 释放鼠标
# ac.release()
#
# # 右键点击
# ac.context_click()

# 双击

# 拖拽

# 按下某键
ac.key_down()

# 松开某键

# # 向元素发送键盘指令
# ac.send_keys_to_element()

sleep(3)

wd.quit()