import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException



chrome_driver_path = os.path.join('chrome drivers/linux64/chromedriver')
user = "beghamiplomb@gmail.com"
password = "AMISKH2022"
target_page = "general.plomberie"
base_url = "https://www.instagram.com"
################################################################################## 
  
driver = webdriver.Chrome(chrome_driver_path)
  
# open the webpage
driver.get(base_url)
  
# target username
username_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='username']")))
  
# target Password
password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='password']")))
  
# enter username and password
username_input.send_keys(user)
password_input.send_keys(password)
# target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()
  
time.sleep(3)
  
#target the page
driver.get(base_url+"/"+target_page+"/"+"followers")


driver.find_element_by_partial_link_text("follower").click()


pop_up_window = WebDriverWait(
    driver, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='isgrP']")))

print(pop_up_window)


def follow():
    all_buttons = driver.find_elements(by=By.CSS_SELECTOR , value='li button')
    for button in all_buttons:
        try:
            button.click()
            time.sleep(5)
        except ElementClickInterceptedException:
            cancel_button = driver.find_element(by=By.XPATH , value='/html/body/div[7]/div/div/div/div[3]/button[2]')
            time.sleep(5)
            cancel_button.click()


def scroll():
    for i in range(50):
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
        pop_up_window)


time.sleep(1)
# Scroll till Followers list is there
while True :
    follow()
    scroll()
    
  
driver.quit()