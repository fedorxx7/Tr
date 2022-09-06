import telegram
import picamera

# Connect to our bot
bot = telegram.Bot(token="123456789:ABCDabcdefgYGscai2d_hakusnci7Hdks")

# Sets the id for the active chat
chat_id=123456789

#Get the photo
camera=picamera.PiCamera()
camera.capture('./capture.jpg')
camera.close()

# Sends a message to the chat
bot.sendPhoto(chat_id=chat_id, photo=open('./capture.jpg', 'rb'))
