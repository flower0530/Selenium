from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get("http://www.unixde.com/")
wd.implicitly_wait(3)

button_nums = wd.find_elements(By.CSS_SELECTOR,"button")
img_nums = wd.find_elements(By.CSS_SELECTOR,"img")
sum_nums = wd.find_elements(By.CSS_SELECTOR,"button,img")

print(f"按钮数={len(button_nums)}")
print(f"图片数={len(img_nums)}")
print(f"总数={len(sum_nums)}")
if len(button_nums)+len(img_nums) == len(sum_nums):
    print("正确！")

print("--------------------------------------------")


ele1 = wd.find_elements(By.CSS_SELECTOR,'[class="banner__inner"] .zz-comp,div')
ele2 = wd.find_elements(By.CSS_SELECTOR,'[class="banner__inner"] .zz-comp,[class="banner__inner"] div')

print(f"banner__inner类中类为zz-comp数和所有元素中有div标签数之和={len(ele1)}")
print(f"banner__inner类中类为zz-comp数和含有div标签数之和={len(ele2)}")
if len(ele1) > len(ele2):
    print("正确！")


wd.quit()