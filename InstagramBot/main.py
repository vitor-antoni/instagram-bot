import  time
import Functions


username = str("user_email")
password = str("user_password")
postLink = str("post_link")

Functions.setUserInformations(username, password)

print("Hi, welcome to the instagram-bot!!! :D")
time.sleep(1.5)

Functions.iniciarNavegador()

Functions.loginFacebook()

Functions.goToLink(postLink)

Functions.createComent()

print("Finished!! :D")