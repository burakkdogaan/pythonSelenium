from selenium import webdriver

import time

browser = webdriver.Firefox()
browser.get("https://twitter.com/")
time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span")
giris_yap.click()

time.sleep(5)
email_giris = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a")
email_giris.click()
time.sleep(5)
username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
username.send_keys("yourUsername")
password.send_keys("yourPassword")
time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span")
login.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")

searchArea.send_keys("#yazilimayolver")
searchArea.send_keys(u'\ue007')

time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while (match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    if lastCount == lenOfPage:
        match = True
time.sleep(5)

i = 0
while i < 500:
    try:
        liker = browser.find_element_by_css_selector("[data-testid=like]")
        liker.click()
        i += 1
    except:
        pass

browser.close()