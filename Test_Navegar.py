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
time.sleep(1);

driver.get("https://www.youtube.com/c/HomosapiensYT/videos")
time.sleep(1);

#regresar a pagina anterior, puede generar problemas si hay un sleep > 4 seg
#driver.back();
driver.execute_script("window.history.go(-1)")
time.sleep(1);

#ir adelante, forward tambien puede generar problemas con el sleep
#driver.forward()
driver.execute_script("window.history.go(1)")


driver.close()