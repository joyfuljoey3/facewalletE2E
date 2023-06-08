#Ch_selenium/example/tutorial1.py
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import argparse, sys

import time

# argument parser
parser=argparse.ArgumentParser()
parser.add_argument("--email", help="Google Login email", type= str)
parser.add_argument("--pw", help="Google Login password", type= str)
parser.add_argument("--pin", help="6 digit pin number", type= str)

args=parser.parse_args()


driver = uc.Chrome()
driver.get("https://haechi-labs.github.io/face-sample-dapp/")

# Connet network (connect to Baobob)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[8]').click()
# get iframe(Secend frame)
iframe = driver.find_element(By.XPATH, '/html/body/iframe')


# login
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div').click()

# Switch to iframe
driver.switch_to.frame(iframe)
#  wait for new div
WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]'))
)

# click google login
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/button[1]').click()
#driver.find_element(By.CSS_SELECTOR, '#root > div > div.css-fxnstr > div > div > div > div.face-body.css-1pvcssm > div.css-xi606m > div.css-1vvrxth > button:nth-child(1) > div').click()

original_window = driver.current_window_handle
for win_handle in driver.window_handles:
    if win_handle != original_window:
        driver.switch_to.window(win_handle)
        break


WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
)
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(args.email)
WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))
)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(0.5)
WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
)
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(args.pw)
WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
)
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
time.sleep(1)

driver.switch_to.window(original_window)
time.sleep(1)
driver.switch_to.frame(iframe)
time.sleep(1)
# wait for pin pad to show up
WebDriverWait(driver,20).until(
    # EC.find_element((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]/div/div[7]'))
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]/div/div[7]'))
)
time.sleep(0.5)

# enter Pin using --pin argument
for num in args.pin:
    xpath = '//*[contains(text(),'+num+')]'
    driver.find_element(By.XPATH, xpath).click()

# wait for login complete message to show up
WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Continue")]'))
)
time.sleep(0.5)

# click continue button
driver.find_element(By.XPATH, '//*[contains(text(),"Continue")]').click()
time.sleep(0.5)

#switch_to.default_content()
driver.switch_to.default_content()

WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Address: ")]'))
)

#amount clear
coin_amount = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div/div[1]/div[2]/div/p/input')
coin_amount.clear();
coin_amount.send_keys("1")


driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div/div[3]').click()

driver.switch_to.frame(iframe)
WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Send Now")]'))
)

driver.find_element(By.XPATH, '//*[contains(text(),"Send Now")]').click()

WebDriverWait(driver,20).until(
    # EC.find_element((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[2]/div/div[7]'))
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]'))
)

for num in args.pin:
    xpath = '//*[contains(text(),'+num+')]'
    driver.find_element(By.XPATH, xpath).click()


time.sleep(0.5)

time.sleep(10)
