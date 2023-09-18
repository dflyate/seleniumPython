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
driver.get("https://demoqa.com/")
driver.maximize_window()
t=2

#comprueba si existe o no una imagen para hacer un clic sobre un boton
titulo=driver.find_element(By.XPATH,'//*[@id="app"]/header/a/img')
btn1=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[1]')
if(titulo.is_displayed()==True):
    print("existe la imagen")
    btn1.click();
else:
    print("existe la imagen")

time.sleep(t)
driver.close()