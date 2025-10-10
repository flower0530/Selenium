from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get("http://www.unixde.com/")
wd.implicitly_wait(3)


ele1 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]+div")
ele2 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]~div")

print(len(ele1))
print(len(ele2))

wd.quit()