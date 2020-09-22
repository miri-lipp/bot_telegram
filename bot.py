import telegram
bot = telegram.Bot(token = '1313430420:AAG24E5iOg0JyGVgxyC9eQha75tYxUSUunE')
print(bot.get_me())
{"first_name": "Toledo's Palace Bot", "username": "ToledosPalaceBot"}
import logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

from telegram.ext import Updater
from telegram.ext import CommandHandler
updater = Updater(token = '1313430420:AAG24E5iOg0JyGVgxyC9eQha75tYxUSUunE', use_context = True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

def start(update, context):
	context.bot.send_message(chat_id = update.effective_chat_id, text = "I'm a bot, please talk to me!")

