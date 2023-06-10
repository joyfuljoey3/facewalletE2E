
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse, sys
import time
# for google login
import undetected_chromedriver as uc


args = None


def init_driver():
    driver = uc.Chrome()
    driver.get('https://haechi-labs.github.io/face-sample-dapp/')
    return driver

def do_login(driver):
    # Connet network (connect to Baobob)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[8]').click()

    # get iframe(Secend frame)
    iframe = driver.find_element(By.XPATH, '/html/body/iframe')


    # login button click
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

    # wait for google login Email input area
    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    )
    # input email
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(args.email)

    # wait for next button
    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))
    )
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(0.5)

    # wait for google login password input area
    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    time.sleep(0.5)
    # input password
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(args.pw)

    # wait for next button
    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
    )
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(1)

    # return to original window
    driver.switch_to.window(original_window)
    time.sleep(1)
    # switch to iframe
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
    time.sleep(1)

    # click continue button
    driver.find_element(By.XPATH, '//*[contains(text(),"Continue")]').click()
    time.sleep(0.5)
    driver.switch_to.default_content()

def coin_tranaction(driver):

    # After login find Address text
    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Address: ")]'))
    )

    # defailt amount clear & input "0.1"
    coin_amount = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div/div[1]/div[2]/div/p/input')
    coin_amount.clear();
    coin_amount.send_keys("0.1")

    # defailt eoa clear & input "0x758B82e64B597715c6Edd3de56074a4914E10B7F"
    from_address = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div/div[2]/div[2]/div/p/input')
    from_address.clear();
    from_address.send_keys("0x758B82e64B597715c6Edd3de56074a4914E10B7F")

    # Click button
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/div/div[3]').click()

    # get iframe(Secend frame)
    iframe = driver.find_element(By.XPATH, '/html/body/iframe')

    driver.switch_to.frame(iframe)
    # wait for transaction confirm page
    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Send Now")]'))
    )
    time.sleep(0.5)
    #click "send now" button
    driver.find_element(By.XPATH, '//*[contains(text(),"Send Now")]').click()

    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]'))
    )
    time.sleep(0.5)

    # enter Pin using --pin argument
    for num in args.pin:
        xpath = '//*[contains(text(),'+num+')]'
        driver.find_element(By.XPATH, xpath).click()

    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Success!")]'))
    )
    time.sleep(0.5)

    # click X button
    driver.find_element(By.CLASS_NAME, 'css-dzm4av').click()
    time.sleep(0.5)

    #return to original frame
    driver.switch_to.default_content()

    # wait for Explorer Link
    WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Explorer Link")]'))
    )
    #click Explorer Link
    driver.find_element(By.XPATH, '//*[contains(text(),"Explorer Link")]').click()

if  __name__  ==  "__main__" :
    # argument parser
    parser=argparse.ArgumentParser()
    parser.add_argument("--email", help="Google Login email", type= str)
    parser.add_argument("--pw", help="Google Login password", type= str)
    parser.add_argument("--pin", help="6 digit pin number", type= str)
    args=parser.parse_args()

    driver = init_driver()
    do_login(driver)
    coin_tranaction(driver)



time.sleep(10)
