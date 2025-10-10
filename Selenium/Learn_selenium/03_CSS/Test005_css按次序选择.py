from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get("http://www.unixde.com/")
wd.implicitly_wait(3)

A1 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]:nth-child(2)")
A2 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]:nth-last-child(2)")
B1 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]:nth-of-type(2)")
B2 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]:nth-last-of-type(2)")
C1 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]:nth-child(even)")
C2 = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]:nth-child(odd)")
C = wd.find_elements(By.CSS_SELECTOR,"[class*=zz]")

print(len(A1))
print(len(A2))
print(len(B1))
print(len(B2))
print(len(C1))
print(len(C2))
print(len(C))
if len(C1) + len(C2) == len(C):
    print("正确！")

wd.quit()