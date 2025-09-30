import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化
wd = webdriver.Chrome()
wd.get("http://www.unixde.com/")
wd.implicitly_wait(20)

# 定位元素，id/class/tag
# id
ele1 = wd.find_element(By.CSS_SELECTOR,'#render')
# class
ele2 = wd.find_element(By.CSS_SELECTOR,'.render-v2')
# tag
ele3 = wd.find_element(By.CSS_SELECTOR,'div')
# 打印验证
print(ele1.get_attribute('outerHTML'))
print("=========================")
print(ele1.text)
print("=========================")
print(ele1.text)

# # 全部文本
# ele3 = wd.find_element(By.CSS_SELECTOR,'body')
# print(ele3.get_attribute('textContent'))

# 等待并退出
# time.sleep(10)
wd.quit()