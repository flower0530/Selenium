# from selenium import webdriver  # 需要添加这一行来导入webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC  # 也需要导入expected_conditions
# import time
# browser = webdriver.Edge()
# browser.get("http://192.168.2.80:9530/login")
#
# browser.implicitly_wait(5)
#
# # 1. 账号输入框（第一个）
# username_input = browser.find_elements(By.CLASS_NAME, "el-input__inner")[0]
# username_input.send_keys("Superadmin")
#
# # 2. 密码输入框（第二个）
# password_input = browser.find_elements(By.CLASS_NAME, "el-input__inner")[1]
# password_input.send_keys("soyotec@00")  # 替换为真实密码
#
# # 验证码，需手动输入
# time.sleep(6)
#
# # 找到包含“登录”的按钮
# login_button = browser.find_element(By.XPATH, "//button//span[text()='登 录']")
# login_button.click()
#
# time.sleep(5)
#
# browser.quit()

# import easygui
#
# user_input = easygui.enterbox("请输入验证码:", '输入窗口')
# print(f'用户输入为：{user_input}')

