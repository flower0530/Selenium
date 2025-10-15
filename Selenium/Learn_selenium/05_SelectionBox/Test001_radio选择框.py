from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.implicitly_wait(3)
wd.get("https://www.byhy.net/cdn2/files/selenium/test2.html")

radios = wd.find_elements(By.CSS_SELECTOR,"#s_radio input")
print(f"一共找到{len(radios)}个radio组件!")

# 缺省
checked_radio1 = wd.find_element(By.CSS_SELECTOR,"#s_radio input[checked]")
print("缺省选中的radio的value内容为：" + checked_radio1.get_attribute('value'))

# 点击、当前选中
check_radio1 = wd.find_element(By.CSS_SELECTOR,"#s_radio input:checked")
print("当前选中的是：" + check_radio1.get_attribute('value'))
radios[1].click()
print("完成点击！")
check_radio2 = wd.find_element(By.CSS_SELECTOR,"#s_radio input:checked")
print("当前选中的是：" + check_radio2.get_attribute('value'))

# 缺省
checked_radio2 = wd.find_element(By.CSS_SELECTOR,"#s_radio input[checked]")
print("缺省选中的radio的value内容为：" + checked_radio2.get_attribute('value'))

wd.quit()