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
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
t=2

driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a").click()
time.sleep(t)

try:
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="myModal0"]/div/div/div[4]/a[2]')))
    driver.find_element(By.XPATH,'//*[@id="myModal0"]/div/div/div[4]/a[2]').click()
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta")
time.sleep(t)
driver.close()