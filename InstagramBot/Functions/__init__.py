import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setUserInformations(username, password):
    global usernameLogin, passwordLogin
    usernameLogin = username
    passwordLogin = password

def iniciarNavegador():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/vsilv/OneDrive/Documentos/chromedriver.exe")
    driver.get("https://www.instagram.com/accounts/login/")

    time.sleep(3)

def loginFacebook():
    try:
        botaoLogin = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[5]/button/span[2]")
        botaoLogin.click()
    except:
        botaoLogin = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[5]/button/span[2]")
        botaoLogin.click()

    time.sleep(2)

    inputUsername = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(usernameLogin)

    time.sleep(0.5)

    inputPassword = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(passwordLogin)

    time.sleep(1)

    joinAccount = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button")
    joinAccount.click()

    time.sleep(12)

    turnOfNotifications = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
    turnOfNotifications.click()