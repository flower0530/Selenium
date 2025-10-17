from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

wd = webdriver.Edge()
wd.implicitly_wait(3)
wd.get("https://www.byhy.net/cdn2/files/selenium/test2.html")

# print(len(wd.find_elements(By.CSS_SELECTOR,'select')))
sel1 = wd.find_elements(By.CSS_SELECTOR,'select')[0]
sel2 = wd.find_elements(By.CSS_SELECTOR,'select')[1]

select1 = Select(sel1)
select2 = Select(sel2)


# 区分单选、多选
multiple = wd.find_elements(By.CSS_SELECTOR,'select[multiple]')
print(f"多选框有{len(multiple)}个")

# 缺省
print("单选框的默认选择元素为：" + sel1.find_element(By.CSS_SELECTOR,'[selected]').get_attribute('value'))
print("多选框的默认选择元素为：" + sel2.find_element(By.CSS_SELECTOR,'[selected]').get_attribute('value'))

# 当前选中


# 所有元素
options1 = select1.all_selected_options
options2 = select2.all_selected_options
print(options1)
# for option in options1:
#     print(option.text)
# for option in options2:
#     print(option.text)

# 选中

# 去选


wd.quit()