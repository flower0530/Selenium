from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 单选框
wd = webdriver.Edge()
wd.get("http://192.168.2.80:9527")
wd.implicitly_wait(3)
# 账号组件
account_input = wd.find_element(By.CSS_SELECTOR,'[placeholder="手机号/邮箱/用户名"]')
# 密码组件
password_input = wd.find_element(By.CSS_SELECTOR,'[placeholder="密码"]')
# 登录
login_button = wd.find_element(By.CSS_SELECTOR,'[class="el-button login-submit el-button--primary el-button--small"]')
# 输入
account_input.send_keys('Superadmin')
password_input.send_keys('soyotec@00')
# 手动输入验证码后回车登录
input("回车继续")
sleep(2)
login_button.click()

# 展开数据集管理进入列表页
Sj1 = wd.find_elements(By.CSS_SELECTOR,'[role=menuitem]')[1]
Sj1.click()
Sj2 = wd.find_elements(By.CSS_SELECTOR,'[role=menuitem]')[2]
Sj2.click()


sleep(8)
wd.quit()
