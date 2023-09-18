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

nom=driver.find_element(By.ID,"userName")
nom.send_keys("Daniel")
nom.send_keys(Keys.TAB + "dflyate@gmail.com"+Keys.TAB + "calle falsa"+Keys.TAB + "falllle"+Keys.TAB + Keys.ENTER)
time.sleep(1)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(10);

driver.close()