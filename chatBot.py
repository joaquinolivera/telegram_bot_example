import requests
from requests import get
import re
import logging
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters

def get_url():
	contents = requests.get('https://random.dog/woof.json').json()    
	url = contents['url']
	return url

def get_image_url():
	allowed_extension = ['jpg','jpeg','png']
	file_extension = ''
	while file_extension not in allowed_extension:
		url = get_url()
		file_extension = re.search("([^.]*)$",url).group(1).lower()
	return url

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def master(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Hi Master! I'm your first python bot for telegram")

def echo(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def bop(update, context):
	url = get_image_url()
	context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def caps(update, context):
	text_caps = ' '.join(context.args).upper()
	context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def main():
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	updater = Updater('YOUR:TOKEN', use_context=True)
	dp = updater.dispatcher
	start_handler = CommandHandler('start', start)
	dp.add_handler(start_handler)
	joaquin_handler = CommandHandler('master', master)
	dp.add_handler(joaquin_handler)
	caps_handler = CommandHandler('caps', caps)
	dp.add_handler(caps_handler)
	bop_handler = CommandHandler('bop', bop)
	dp.add_handler(bop_handler)
	echo_handler = MessageHandler(Filters.text, echo)
	dp.add_handler(echo_handler)
	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()
    
if __name__ == '__main__':
	main()
