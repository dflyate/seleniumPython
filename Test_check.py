from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='G:\PROGRAMACION\SELENIUM CON PYTHON\Drivers\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
t=5
bt1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tree-node"]/ol/li/span/label/span[1]')))
bt1.click()
time.sleep(t)
