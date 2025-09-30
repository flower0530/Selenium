import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化
wd = webdriver.Edge()
wd.get("http://www.unixde.com/")
wd.implicitly_wait(3)

# 定位
elements1 = wd.find_elements(By.CSS_SELECTOR,'[href]')
elements2 = wd.find_elements(By.CSS_SELECTOR,'[href*=mdo]')
elements3 = wd.find_elements(By.CSS_SELECTOR,'[href^=http]')
elements4 = wd.find_elements(By.CSS_SELECTOR,'[href$=".com"]')
element5 = wd.find_element(By.CSS_SELECTOR,'.zz-comp[class="zz-comp zz-comp-text clearfix _1cutbktago010"][data-type*=te] > div p > a[href*=http]')

# 打印
print(f"网页中共包含“[href]”属性的有：{len(elements1)}条!")
i = 1
for ele in elements1:
    print(f"第{i}条： {ele.get_attribute('href')}")
    i += 1
print("========================================================")

print(f"网页中共包含“[href]”且值中含有“mdo”的有：{len(elements2)}条!")
i = 1
for ele in elements2:
    print(f"第{i}条： {ele.get_attribute('href')}")
    i += 1
print("========================================================")

print(f"网页中共包含“[href]”且以“http”开头的有：{len(elements3)}条!")
i = 1
for ele in elements3:
    print(f"第{i}条： {ele.get_attribute('href')}")
    i += 1
print("========================================================")

print(f"网页中共包含“[href]且以“.com/”结尾的有”：{len(elements4)}条!")
i = 1
for ele in elements4:
    print(f"第{i}条： {ele.get_attribute('href')}")
    i += 1
print("========================================================")

print("网页中符合定位条件的元素文字内容为:" +element5.text + "!")
element5.click()
time.sleep(10)

# 等待并退出
# time.sleep(10)
wd.quit()