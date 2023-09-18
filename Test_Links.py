from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

service = Service(executable_path='G:\PROGRAMACION\SELENIUM CON PYTHON\Drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t=2

#Obteniendo todos los links de la pagina
links=driver.find_elements(By.TAG_NAME,"a")
print("el numero de links de la pagina es "+str(len(links)))
for num in links:
    print(num.text)
driver.find_element(By.LINK_TEXT,"Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT,"JQuery Date Picker").click()
time.sleep(t)
driver.close()