import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get("https://www.unixde.com")

wd.implicitly_wait(5)

elements = wd.find_elements(By.CLASS_NAME,"zz-submenu")
print("根据ID查找到Class名为“zz-submenu”的是:")
print(elements)

count_all = 0
count_value = 0

for ele in elements:
    count_all += 1
    if ele.text:
        print(ele.text)
        count_value += 1

print("总条数：" + str(count_all))
print("非空条数：" + str(count_value))

time.sleep(10)
wd.quit()