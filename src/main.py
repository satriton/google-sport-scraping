import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from extractData import extract_game_data_from_html

# Configure headless options
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()

search = "Stade toulousain"
url = f'https://google.com/search?q={search}'

driver.get(url)
# from selenium.webdriver import ActionChains

# wait = WebDriverWait(driver, 10) # wait up to 4s
# element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "SwsxUd")))
# action = ActionChains(driver)
# action.move_to_element(element).click().perform()
# # element.click()
# # driver.execute_script("arguments[0].click();", element)

data = BeautifulSoup(driver.page_source, 'html.parser')

games = data.find_all('table', class_='KAIX8d')
print(len(games))

# Print the data objects
for game_html in games:
    print("------")
    print(extract_game_data_from_html(game_html))


driver.quit()
