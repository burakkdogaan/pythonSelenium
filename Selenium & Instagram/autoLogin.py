from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(2)


username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("yourUsername")
password.send_keys("yourPassword")

loginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
loginButton.click()

time.sleep(5)

profileButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")

profileButton.click()
time.sleep(5)
profileDetail = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]")
profileDetail.click()

time.sleep(6)
followersDetail = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followersDetail.click()

time.sleep(5)


jscommand = """
    followers = document.querySelector("._1XyCr ");
    followers.scrollTo(0, followers.scrollHeight);
    var lenOfPage=followers.scrollHeight;
    return lenOfPage;
    

"""
lenOfPage = browser.execute_script(jscommand)
match = False
while (match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)

    if lastCount == lenOfPage:
        match = True
time.sleep(5)

followerList = []
followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
for follower in followers:
    followerList.append(follower.text)

with open("followers.txt", "w", encoding="UTF-8") as file:
    for follower in followerList:
        file.write(follower + "\n")



browser.close()

