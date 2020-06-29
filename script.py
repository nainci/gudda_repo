names = [
    "Naina",
    "Soumya",
    "Shivi",
    "Ashish",
    "Shivali",
    "Ankita",
    "Apoorva",
    "Abhishek",
    "Vipul",
    "Sachin",    
    "Vidhi",
    "Sonal",
    "Soniya",
    "Viren",
    "Bhavana",
    "Archana",
    "Sanjana",
    "Janhvi",
]
import random

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

from selenium import webdriver
import time

successful_votes = 0
while True:

    # webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    #     "httpProxy": proxy,
    #     "ftpProxy": proxy,
    #     "sslProxy": proxy,
    #     "proxyType": "MANUAL",

    # }

    # driver = webdriver.Firefox(executable_path=f"./geckodriver-v0.26.0-win64/geckodriver.exe")
    # driver.implicitly_wait(30)
    # driver.maximize_window()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    driver = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    driver.get("https://mycutebaby.in/contest/participant/?n=5eebb94df11e1")
    time.sleep(15)
    username = driver.find_element_by_id("v")
    name = random.sample(names, 1)[0]
    username.send_keys(name)
    print("Clicking", name)
    driver.find_element_by_id("vote_btn").click()
    time.sleep(3)
    vote_msg = driver.find_element_by_id("vote_msg").text
    
    if "Thank you" in vote_msg:
        successful_votes += 1
        print(f"Successfully voted {successful_votes} times")
    else:
        print(f"Some error")

    driver.close()
    driver.quit()

    # break
    time.sleep(60 * 31)
