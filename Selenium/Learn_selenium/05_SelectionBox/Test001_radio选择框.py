from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 单选框
wd = webdriver.Edge()
wd.get("http://192.168.2.80:9527")
wd.implicitly_wait(3)
account_input = wd.find_element(By.CSS_SELECTOR,'[placeholder="手机号/邮箱/用户名"]')
password_input = wd.find_element(By.CSS_SELECTOR,'[placeholder="密码"]')
login_button = wd.find_element(By.CSS_SELECTOR,'[class="el-button login-submit el-button--primary el-button--small"]')
account_input.send_keys('Superadmin')
password_input.send_keys('soyotec@00')
sleep(6)
login_button.click()

list1 = wd.find_element(By.CSS_SELECTOR,'[href="/dtm-app/dtm/dataSetManagement/dataSetList"]')
list1.click()

sleep(10)
wd.quit()
