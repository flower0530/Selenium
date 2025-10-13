from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("https://www.byhy.net/cdn2/files/selenium/sample2.html")

# 原frame搜索plant个数
ele1 = wd.find_elements(By.CSS_SELECTOR,'.plant')
print(f"原frame搜索plant个数为：{len(ele1)}")

# 找到新的frame元素
new_frame = wd.find_element(By.CSS_SELECTOR,'[src="sample1.html"]')

# 切换窗口
wd.switch_to.frame(new_frame)
print("成功切换新的frame")
ele2 = wd.find_elements(By.CSS_SELECTOR,'.plant')
print(f"新的frame搜索plant个数为：{len(ele2)}")

# 切换回原frame
wd.switch_to.default_content()
print("成功切换原frame")
ele3 = wd.find_elements(By.CSS_SELECTOR,'.plant')
print(f"原frame搜索plant个数为：{len(ele3)}")

wd.quit()