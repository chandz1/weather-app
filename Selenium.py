from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Path = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get("https://www.timeanddate.com/weather/")

search = driver.find_element_by_id("sb_wc_q")
search.send_keys("hyderabad")
search.send_keys(Keys.RETURN)

try:
    places = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "tbody"))
    )
    print(places.text)
except:
    driver.quit()
