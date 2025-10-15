from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.implicitly_wait(3)
wd.get("https://www.byhy.net/cdn2/files/selenium/test2.html")

radios = wd.find_elements(By.CSS_SELECTOR,'#s_checkbox > input')
print(f"找到 {len(radios)} 个checkBox选择框")

# 缺省
checked = wd.find_element(By.CSS_SELECTOR,'#s_checkbox > input[checked]')
print(checked.get_attribute('value'))

# 当前选中，
checks = wd.find_elements(By.CSS_SELECTOR,'#s_checkbox > input:checked')
for check in checks:
    print(check.get_attribute('value'))

# 取消所有选中，点击多个
checks = wd.find_elements(By.CSS_SELECTOR,'#s_checkbox > input:checked')
for check in checks:
    check.click()
radios[0].click()
radios[1].click()

# 当前选中
checks = wd.find_elements(By.CSS_SELECTOR,'#s_checkbox > input:checked')
for check in checks:
    print(check.get_attribute('value'))

wd.quit()