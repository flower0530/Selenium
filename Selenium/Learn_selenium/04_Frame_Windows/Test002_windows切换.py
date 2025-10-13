import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("http://www.baidu.com/")
main_handle = wd.window_handles[0]
print(f"当前窗口的标题为：{wd.title}\n-----------------------------")

# 热搜
hot_button = wd.find_element(By.CSS_SELECTOR,'[src="https://psstatic.cdn.bcebos.com/basics/aichat/hot_search_x3_1747880381000.png"]')
hot_button.click()
hot_handle = wd.window_handles[1]
wd.switch_to.window(hot_handle)
print("已切换热搜窗口")
print(f"当前窗口的标题为：{wd.title}\n-----------------------------")

# 关于百度
aboutBaidu_button = wd.find_element(By.CSS_SELECTOR,'.c-font-small[href="//home.baidu.com"]')
aboutBaidu_button.click()
about_handle = wd.window_handles[2]
wd.switch_to.window(about_handle)
sleep(0.5)
print("已切换关于百度窗口")
print(f"当前窗口的标题为：{wd.title}\n-----------------------------")


wd.switch_to.window(main_handle)
print("已切换原始窗口")
print(f"当前窗口的标题为：{wd.title}\n-----------------------------")

# 遍历输出界面句柄和对应标题
handles = wd.window_handles
print(f"当前共打开{len(handles)}个窗口，具体如下：")
i = 1
for h in handles:
    wd.switch_to.window(h)
    print(f"第{i}个窗口：")
    print(f"标题:{wd.title}")
    print(f"句柄:{h}")
    print("----------------------")
    i += 1

wd.quit()