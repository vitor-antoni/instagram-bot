import  time
import Functions


username = str("user_email")
password = str("user_password")
postLink = str("post_link")

Functions.setUserInformations(username, password)

print("Ola, seja bem vindo ao bot de intagram!!")
time.sleep(1.5)

Functions.iniciarNavegador()

Functions.loginFacebook()

Functions.goToLink(postLink)

Functions.createComent()