import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get("https://www.unixde.com")

# 隐式等待，如果加上，后面循环遍历的时候如果遇到为空的元素，就会很慢，因为会等待
# wd.implicitly_wait(5)

time.sleep(3)

elements = wd.find_elements(By.TAG_NAME,"div")
# print(len(elements))

# 添加这行：配置日志输出到控制台
logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.getLogger().info(len(elements))

i = 1
for ele in elements:
    if ele.text:
        divs = ele.find_elements(By.TAG_NAME, "div")
        print("第" + str(i) + "个div里包含" + str(len(divs)) + "个div")
    i += 1

time.sleep(3)
wd.quit()