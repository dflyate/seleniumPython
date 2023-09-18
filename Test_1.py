from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='G:\PROGRAMACION\SELENIUM CON PYTHON\Drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2);

driver.find_element("xpath","//*[@id='userName']").send_keys("Daniel")
driver.find_element("xpath","//*[@id='userEmail']").send_keys("dflyate@gmail.com")
driver.find_element("xpath","//*[@id='currentAddress']").send_keys("Cll falsa 123")
driver.find_element("xpath","//*[@id='permanentAddress']").send_keys("Cll falsa 123456")
time.sleep(1)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
driver.find_element("xpath","//*[@id='submit']").click()
time.sleep(10);

driver.close()