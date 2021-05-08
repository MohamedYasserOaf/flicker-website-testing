import self as self
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wait_time = 20
cooldown_time = 5
correct_email = "m.yasseroaf@gmail.com"
correct_password = "oxsrakas1998"
user_search = "football"

chrome_driver_path = ".\chromedriver.exe"
self.driver = webdriver.Chrome(chrome_driver_path)

self.driver.get("https://www.flickr.com")  # getting flicker.com
self.driver.maximize_window()  # maximize window

login_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[2]/a")))
login_button.click()  # pressing on the login tab

email_textbox = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[2]/div/input")))
email_textbox.send_keys(correct_email)  # sending email to text box

next_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/button")))
next_button.click()  # pressing on next button

password_textbox = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[3]/div/div/input")))
password_textbox.send_keys(correct_password)  # sending password to text box

signin_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/button/span")))
signin_button.click()

time.sleep(cooldown_time)

search_bar = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[1]/div/form/input")))
search_bar.send_keys(user_search)

search_bar_button = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[2]/li[1]/div/form/label/input")))
search_bar_button.submit()

photos_listitem = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul[1]/li[1]")))
photos_listitem.click()

press_on_photo = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[2]/div[1]/div/div/a"))).get_attribute("href")
self.driver.get(press_on_photo)

action = ActionChains(self.driver)

fav_photo = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[5]/div[1]/div/a")))

action.move_to_element(fav_photo).click().perform()
time.sleep(5)

see_favs = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div[3]/div[1]/div/a[3]")))
see_favs.click()
