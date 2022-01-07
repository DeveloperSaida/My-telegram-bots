from telegram.ext import Updater,CommandHandler
from telegram.ext import MessageHandler,Filters
from methods import start,xabar

updater=Updater(token="5049460475:AAFGIZF6PIdb0NzM6t8okikjQLh-zNnEMQQ",use_context=True)

dispatcher=updater.dispatcher

start_handler=CommandHandler('start',start)
message_handler=MessageHandler(Filters.text,xabar)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
print('Ok,bot yaxshi ishlayabdi')