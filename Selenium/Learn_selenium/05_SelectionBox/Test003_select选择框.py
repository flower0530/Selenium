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
print("---------------------------------------")

# 缺省
print("单选框的默认选择元素为：" + sel1.find_element(By.CSS_SELECTOR,'[selected]').get_attribute('value'))
print("多选框的默认选择元素为：" + sel2.find_element(By.CSS_SELECTOR,'[selected]').get_attribute('value'))
print("---------------------------------------")

# 当前选中
options1_sele = select1.all_selected_options
options2_sele = select2.all_selected_options
print("单选框当前选择为：")
for option in options1_sele:
    print(option.text)
print("多选框当前选择为：")
for option in options2_sele:
    print(option.text)
print("---------------------------------------")

# 所有元素
options1 = select1.options
options2 = select2.options
print("单选框所有选择为：")
for option in options1:
    print(option.text)
print("多选框所有选择为：")
for option in options2:
    print(option.text)
print("---------------------------------------")

# 选中/去选
# 单选框
print("单选框选择小雷老师")
select1.select_by_index(0)
select1.select_by_value('小雷老师')
select1.select_by_visible_text('小江老师')
# 多选框
print("多选框全选")
select2.deselect_all()
select2.select_by_index(0)
select2.select_by_value('小雷老师')
select2.select_by_visible_text('小凯老师')
print('----------------------------------------')

# 当前选中
options1_sele = select1.all_selected_options
options2_sele = select2.all_selected_options
print("单选框当前选择为：")
for option in options1_sele:
    print(option.text)
print("多选框当前选择为：")
for option in options2_sele:
    print(option.text)
print("---------------------------------------")

print(select2.is_multiple)
print(select2.first_selected_option.text)

wd.quit()