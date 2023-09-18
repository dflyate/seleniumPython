from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='G:\PROGRAMACION\SELENIUM CON PYTHON\Drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
#espera durante n segundos un objeto (el userNam no existe), por lo tanto lanzara error despues de ese tiempo
#si el id estuviera bien puesto (userName), no se va a demorar los 10 seg
driver.implicitly_wait(10)
time.sleep(2);

driver.find_element("xpath","//*[@id='userNam']").send_keys("Daniel")
driver.find_element("xpath","//*[@id='userEmail']").send_keys("dflyate@gmail.com")
driver.find_element("xpath","//*[@id='currentAddress']").send_keys("Cll falsa 123")
driver.find_element("xpath","//*[@id='permanentAddress']").send_keys("Cll falsa 123456")
time.sleep(1)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
driver.find_element("xpath","//*[@id='submit']").click()
time.sleep(10);

driver.close()