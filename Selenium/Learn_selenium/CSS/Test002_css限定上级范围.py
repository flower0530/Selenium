import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化
wd = webdriver.Edge()
wd.get("http://www.unixde.com/")
wd.implicitly_wait(3)

# 定位
elements = wd.find_elements(By.CSS_SELECTOR,'[data-device="pc"] div.zz-page-body-comp > .zz-comp > .zz-container ._1btmrdc3c8004 > div')
# 打印
print(f"一共有{len(elements)}条符合定位条件！")
for ele in elements:
    print(ele.text)

# 等待并退出
# time.sleep(10)
wd.quit()