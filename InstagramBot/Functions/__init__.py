import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setUserInformations(username, password):
    """
    Esta função irá 'setar' as informações do usuário para login.
    """
    
    global usernameLogin, passwordLogin
    usernameLogin = username
    passwordLogin = password

def iniciarNavegador():
    """
    Esta função irá inicializar o navegador Google Chrome Browser.
    """
    
    global driver
    driver = webdriver.Chrome(executable_path="InstagramBot/chromedriver.exe")
    driver.get("https://www.instagram.com/accounts/login/")

    time.sleep(3)

def loginFacebook():
    """
    Esta função irá realizar o login do usuário pelo Facebook.
    """
    
    try:
        botaoLogin = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[5]/button/span[2]")
        botaoLogin.click()
    except:
        botaoLogin = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[5]/button/span[2]")
        botaoLogin.click()

    time.sleep(2)

    try:
        inputUsername = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(usernameLogin)
    except Exception as error:
        print("Houve um erro para digitar o nome/email do usuário! Erro: " + error)

    time.sleep(0.5)

    try:
        inputPassword = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(passwordLogin)
    except Exception as error:
        print("Houve um erro para digitar a senha do usuário! Error: " + error)
    
    time.sleep(1)

    try:
        joinAccount = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button")
        joinAccount.click()
    except Exception as error:
        print("Houve um erro para clicar no botão de Entrar! Erro: " + error)

    time.sleep(12)

    try:
        turnOfNotifications = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
        turnOfNotifications.click()
    except Exception as error:
        print("Houve um erro para clicar no botão de desativar notificações! Erro: " + error)

    time.sleep(2)

def goToLink(postLink):
    from pyautogui import hotkey
    from pyautogui import write
    from pyautogui import press

    hotkey("ctrl", "t")

    write(postLink)

    press("enter")
