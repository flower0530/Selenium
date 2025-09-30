import time

from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Edge()
wd.get("https://www.unixde.com")

wd.implicitly_wait(5)
time.sleep(3)

elements = wd.find_elements(By.TAG_NAME,"div")
print("获取的元素个数为：" + str(len(elements)))

print("有内容的元素如下:")

count = 0
i = 1

for ele in elements:
    if ele.text:
        print(  "第" + str(i) + "个元素的文本内容为：" + ele.text)
        count += 1
    i += 1

print("总共有内容的条数为：" + str(count) + "条")

time.sleep(3)
wd.quit()