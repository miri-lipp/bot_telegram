import telegram
bot = telegram.Bot(token = '1313430420:AAG24E5iOg0JyGVgxyC9eQha75tYxUSUunE')
print(bot.get_me())
{"first_name": "Toledo's Palace Bot", "username": "ToledosPalaceBot"}

from telegram.ext import Updater
updater = Updater(token = '1313430420:AAG24E5iOg0JyGVgxyC9eQha75tYxUSUunE', use_context = True)
dispatcher = updater.dispatcher

import logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
	context.bot.send_message(chat_id = update.effective_chat_id, text = "В армию хочешь?")
	