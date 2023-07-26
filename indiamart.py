from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
import pandas as pd
website = "https://my.indiamart.com/"
username = "#enteryourusernamehere"
password = "#enteryourpasswordhere"
path = 'chromedriver'

#setting up the driver
service = Service(executable_path=path)
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
time.sleep(1)

#signing into the account
driver.find_element(By.NAME,"mobile").send_keys(username)
time.sleep(1)
signin = driver.find_element(By.ID, "signInSubmitButton")
signin.click()
time.sleep(2)
login = driver.find_element(By.CSS_SELECTOR,"#res-mob1 > div.loginPage > div.row.bannerRow > div > div.banner-section > div.banner-cta > button")
login.click()
time.sleep(2)
enterpassw = driver.find_element(By.ID,"passwordbtn1")
enterpassw.click()
time.sleep(1)
driver.find_element(By.ID,"usr_password").send_keys(password)
time.sleep(1)
submit = driver.find_element(By.ID,"signWP")
submit.click()
time.sleep(2)
close = driver.find_element(By.ID,"thick_closer")
close.click()
time.sleep(1)
leadm = driver.find_element(By.ID,"message_tab")
leadm.click()
time.sleep(1)
cancel = driver.find_element(By.CSS_SELECTOR, "#message_center_leftsection > div.order_now_intro > div.sugg_sbtxt > div.sbtxt1 > svg")
cancel.click()
time.sleep(1)
menu = driver.find_element(By.CSS_SELECTOR, "#message-threedot > span.bxrd20.icn_bg.txt_cntr.f1.icnhovr")
menu.click()
time.sleep(1)
listview = driver.find_element(By.CSS_SELECTOR,"#thrdot > span:nth-child(5)")
listview.click()
time.sleep(2)

#Scraping Data
#total 6633 records
clicks = 131
results = []
while clicks > 0 :
    cards = driver.find_elements(By.CLASS_NAME,"table-row ")
    for card in cards :
        card.click()
        time.sleep(1)
        name = driver.find_element(By.CSS_SELECTOR, "#left-name_ibx > span > span").text
        mobile = driver.find_element(By.ID, "mob_head_lv").text
        loc = driver.find_element(By.ID, "head_address_lv").text
        membersince = driver.find_element(By.ID, "exp_cnt_lv").text


        if driver.find_element(By.ID, "email_head_lv") :
            email = driver.find_element(By.ID, "email_head_lv").text
        else :
            email = None

        if driver.find_element(By.ID, "cmp_name_lv"):
            company = driver.find_element(By.ID, "cmp_name_lv").text

        else :
            company = None

        if driver.find_element(By.CLASS_NAME, "user_txt") :
            try :
                requirement = driver.find_element(By.XPATH, '//*[@id="myenqtab"]/div[1]/div[2]/div[1]/div[3]').text
            except :
                requirement = ""

        else :
            requirement = ""

        time.sleep(1)
        temp = [name, mobile, email, company, requirement, loc, membersince ]
        time.sleep(1)
        results.append(temp)
        print(temp)
        back = driver.find_element(By.CSS_SELECTOR, "#detail_back_btn")
        back.click()
        time.sleep(1)


    time.sleep(2)
    clicks -= 1
    time.sleep(1)
    next = driver.find_element(By.CSS_SELECTOR, "#nextpageclick")
    next.click()
    time.sleep(1)

time.sleep(4)
df = pd.DataFrame(results)
df.columns = ["name", "mobile", "email", "company", "requirement", "location", "membersince"]
df.to_excel("data2.xlsx")