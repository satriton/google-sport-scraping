import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Configure headless options
#options = Options()
#options.add_argument("--headless --incognito")

#driver = webdriver.Chrome(options=options)
driver = webdriver.Firefox()

search = "Stade toulousain"
url = f'https://google.com/search?q={search}'

driver.get(url)

# # Find the <g-fab> element inside <g-immersive-footer> using XPath
# element_xpath = "//g-immersive-footer//g-fab"
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
# element.click()

# # Wait for the new page to load (You might need to adjust the wait time)
# new_page_element_xpath = "//div[contains(@class, 'YIikAd')]"
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, new_page_element_xpath)))


soup = BeautifulSoup(driver.page_source, 'html.parser')

games = soup.find_all('table', class_='KAIX8d')

print(len(games), games[0])
game = games[0]

# Find all rows in the table using the 'tr' tag
rows = soup.find_all('tr')

# Create an empty list to store the data objects
data_objects = []

# Iterate over each row (excluding the header row)
for row in rows[1:]:
    # Extract the necessary data from each row
    columns = row.find_all('td')
    
    team = columns[1].text.strip()
    score = columns[4].text.strip()
    logo = columns[0].find('img')['src']
    date = columns[5].find('span', class_='imspo_mt__cmd').text.strip()
    status = columns[5].find('span', class_='imspo_mt__match-status').text.strip()
    
    video_link = None
    video_element = columns[5].find('a', class_='amp_r')
    if video_element:
        video_link = video_element['data-amp']
    
    # Create a data object with the extracted information
    data_object = {
        'team': team,
        'score': score,
        'logo': logo,
        'date': date,
        'status': status,
        'video_link': video_link
    }
    
    # Append the data object to the list
    data_objects.append(data_object)

# Print the data objects
for data_object in data_objects:
    print(data_object)


driver.quit()
