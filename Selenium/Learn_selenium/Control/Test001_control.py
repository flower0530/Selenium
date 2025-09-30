import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.implicitly_wait(3)
wd.get("http://192.168.2.80:9529/login")
time.sleep(1)

# 获取元素
elements = wd.find_elements(By.CLASS_NAME,"el-input__inner")
username = elements[0]
password = elements[1]
code = elements[2]
loginIn = wd.find_elements(By.CLASS_NAME,"el-button")[0]

# 打印元素属性
print("用户名输入框的“placeholder”属性为：" + username.get_attribute('placeholder'))  # 指定属性
print("登录按钮的“outerHTML”属性为：" + loginIn.get_attribute('outerHTML'))  # 全部属性
print("登录按钮的“innerHTML”属性为：" + loginIn.get_attribute('innerHTML'))  # 内部属性
print("登录按钮的“text”属性为：" + loginIn.text)  # text属性
print("登录按钮的“innerText”属性为：" + loginIn.get_attribute('innerText'))  # innerText属性
print("登录按钮的“textContent”属性为：" + loginIn.get_attribute('textContent'))  # textContent属性

# 输入内容
username.send_keys("Superadmin")
password.send_keys("soyotec@00")
# 展示清除效果
time.sleep(1)
password.clear()
time.sleep(1)
password.send_keys("soyotec@00")
# 等待，手动输入验证码
time.sleep(6)

# 点击元素
loginIn.click()
time.sleep(3)
wd.refresh()

# 关闭
time.sleep(10)
wd.quit()