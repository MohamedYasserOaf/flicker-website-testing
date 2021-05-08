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

action = ActionChains(self.driver)
you_tab = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[1]/li[1]/a")))
action.move_to_element(you_tab).click().perform()

people_item = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/ul[1]/li[1]/ul/li[10]/a")))
people_item.click()

find_friends = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/p/span/span[4]/a")))
find_friends.click()

follow_flicker_suggestions = WebDriverWait(self.driver, wait_time).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/ul/li[1]/ul/li[1]/p[1]/a[1]")))
follow_flicker_suggestions.click()

time.sleep(10)

unfollow_flicker_suggestions = WebDriverWait(self.driver, 5).until(
    EC.element_to_be_clickable((By.XPATH,
                                "/html/body/div[2]/div/div[2]/div[2]/ul/li[1]/ul/li[1]/p[1]/a[2]")))
unfollow_flicker_suggestions.click()



