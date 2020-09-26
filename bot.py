import telegram
import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = '1313430420:AAG24E5iOg0JyGVgxyC9eQha75tYxUSUunE'
bot = telegram.Bot(TOKEN)
print(bot.get_me())
{"first_name": "Toledo's Palace Bot", "username": "ToledosPalaceBot"} 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
PORT = int(os.environ.get('PORT', 5000))

def start(update, context):
	context.bot.send_message(chat_id = update.effective_chat_id, text = "Hello")

def echo(update, context):
	update.message.reply_text(update.message.text)

def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
	updater = Updater(token = '1313430420:AAG24E5iOg0JyGVgxyC9eQha75tYxUSUunE', use_context = True)
	dispatcher = updater.dispatcher
	start_handler = CommandHandler('start', start)
	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(error)
	dispatcher.add_handler(MessageHandler(Filters.text, echo))
	updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path = TOKEN)
	updater.bot.setWebhook('https://secure-savannah-38296.herokuapp.com/' + TOKEN)

if __name__ == '__main__':
    main()