from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = Options()
chrome_options.add_argument("--headless")
path = Service("/your/path")
driver = Chrome(service=path, options=chrome_options)
driver.get("https://www.w3schools.com/html/html_tables.asp")
try:
	wait = WebDriverWait(driver,5)
	element = wait.until(expected_conditions.presence_of_element_located(
		(By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[3]/div/table/tbody/tr[*]")))
	
	data_table = driver.find_elements(By.XPATH, "/html/body/div[7]/div[1]/div[1]/div[3]/div/table/tbody/tr[*]")
	data_table = [data.text for data in data_table]
	
finally:	
	driver.quit()
