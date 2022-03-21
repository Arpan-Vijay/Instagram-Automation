from ast import keyword
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

driver = webdriver.Chrome('C:/Users/DELL/chromedriver.exe')
driver.get("https://www.instagram.com/?hl=en")

# Target username and password field:
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Clear username and password field before inserting the inputs:
username.clear()
password.clear()

# Enter the username and password of your account:
username.send_keys("arpanvi")
password.send_keys("grandi10magna9310")

# Target and select the login button:
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# Target and select "Not Now button" 2 times as it appears twice before logged in to your instagram account
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

# Target the SearchBox field and search for the specific keyword, in our case it's "cats"
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = '#cats'
searchbox.send_keys(keyword)

# Target the first search result
time.sleep(5) # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

# Scroll down to the page, in this case 4 times of the computer screen
driver.execute_script("window.scrollTo(0,4000);")

# Target all the links with the Tagname and src attribute
images = driver.find_element_by_tag_name("img")
images = [image.get_attribute("src") for image in images]

# Saving images to the computer
path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

# Make the directory in your computer
os.mkdir(path)

# Download images
counter = 0
for image in images:
    save_as = os.path.join(path,keyword[1:] + str(counter)+ '.jpg')
    wget.download(image, save_as)

    counter += 1