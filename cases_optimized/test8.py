
from selenium import webdriver  
driver = webdriver.PhantomJS()  
#driver = webdriver.PhantomJS(executable_path="PATH_OF_PhantomJS")  
driver.get("https://language.chinadaily.com.cn/")
data = driver.title  
print(data)