import time, datetime
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']
       
        print ('Recieved: %s' % command)
       
       
        if command == 'Hi':
            bot.sendMessage (chat_id, str("Hi! How are you?"))
           
        elif command == 'I am fine':
             bot.sendMessage (chat_id, str("That's good"))
             
        elif command == 'What time is it?' :
            bot.sendMessage (chat_id, str(now.hour)+str(":")+str(now.minute))

bot = telepot.Bot('5692123762:AAEntAq2ansHFidQVlEz_vHhDBZzOXJ6yQI')

MessageLoop(bot,handle).run_as_thread
print ("I am listening...")
