import  time
import Functions


username = str("user_email")
password = str("user_password")

Functions.setUserInformations(username, password)

print("Ola, seja bem vindo ao bot de intagram!!")
time.sleep(1.5)

Functions.iniciarNavegador()

Functions.loginFacebook()