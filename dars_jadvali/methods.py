from telegram import ReplyKeyboardMarkup

asosiy_oyna=ReplyKeyboardMarkup([
    ['Dushanba' , 'Seshanba' , 'Chorshanba'],
    ['Payshanba','Juma' , 'Shanba'],
    ['Yakshanba','sinf_rahbari']
],resize_keyboard=True)

def start(update,context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Salom @{user.first_name} mening telegram botimga xush kelibsiz!")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Bu botda 254-maktabning 9-A sinf o`quvchilarining dars jadvali joylashgan,"
                                  "marxamat dars jadvalini bilib olishingiz  😉 ",reply_markup=asosiy_oyna)
    return 1
def dushanba(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bu dushanbaning dars jadvali"\
                            f"\nFizika,\nIngliz tili,\nBiologiya,\nOna tili,\nKimyo,\nRus tili",reply_markup=asosiy_oyna)

def seshanba(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bu seshanbaning dars jadvali"\
                            f"\nGeografiya,\nJahon tarix,\nBiologiya,\nOna tili,\nKimyo,\nRus tili",reply_markup=asosiy_oyna)

def chorshanba(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bu chorshanbaning dars jadvali"\
                            f"\nFizika,\nIngliz tili,\nBiologiya,\nOna tili,\nKimyo,\nRus tili",reply_markup=asosiy_oyna)

def payshanba(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bu payshanbaning dars jadvali"\
                            f"\nFizika,\nIngliz tili,\nBiologiya,\nOna tili,\nKimyo,\nRus tili",reply_markup=asosiy_oyna)

def juma(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"jumaning dars jadvali"\
                            f"\nFizika,\nIngliz tili,\nBiologiya,\nOna tili,\nKimyo,\nRus tili",reply_markup=asosiy_oyna)

def shanba(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bu shanbaning dars jadvali"\
                            f"\nFizika,\nIngliz tili,\nBiologiya,\nOna tili,\nKimyo,\nRus tili",reply_markup=asosiy_oyna)

def yakshanba(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bugun dam oling , dushanbada ko`rishamiz",reply_markup=asosiy_oyna)

def sinf_rahbari(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bizning sinf rabarimiz : Xasanova Salima Hurramovna"\
                             f"\nTel:+998903510135",reply_markup=asosiy_oyna)


from telegram.ext import Updater , Filters, ConversationHandler,CommandHandler
from telegram.ext import  MessageHandler


updater=Updater(token='5068620752:AAGeTsUrW2cmU80edPN-rYuNztl4pRpPJTA' ,use_context=True)
dispatcher=updater.dispatcher
conv_handler=ConversationHandler(
    entry_points=[CommandHandler('start',start)],
    states={
        1: [MessageHandler(Filters.regex('^(Dushanba)$'),dushanba),
        MessageHandler(Filters.regex('^(Seshanba)$'),seshanba),
        MessageHandler(Filters.regex('^(Chorshanba)$'),chorshanba),
        MessageHandler(Filters.regex('^(Payshanba)$'),payshanba),
        MessageHandler(Filters.regex('^(Juma)$'),juma),
        MessageHandler(Filters.regex('^(Shanba)$'),shanba),
        MessageHandler(Filters.regex('^(Yakshanba)$'),yakshanba),
        MessageHandler(Filters.regex('^(sinf_rahbari)$'),sinf_rahbari)]


    },
           fallbacks=[MessageHandler(Filters.text,start)]
)


dispatcher.add_handler(conv_handler)
updater.start_polling()
print("Hammasi yaxshi")
