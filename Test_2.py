from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='G:\PROGRAMACION\SELENIUM CON PYTHON\Drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2);

driver.find_element(By.ID,"userName").send_keys("Daniel")
driver.find_element("id","userEmail").send_keys("dflyate@gmail.com")
driver.find_element("id","currentAddress").send_keys("calle falsa")
driver.find_element("id","permanentAddress").send_keys("falllle")
time.sleep(1)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='submit']").click()
time.sleep(10);

driver.close()