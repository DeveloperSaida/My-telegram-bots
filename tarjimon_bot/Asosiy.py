from googletrans import Translator

def translate(matn):
    translator=Translator()
    til=translator.detect(matn).lang
    if til=='en'
        return translator.translate(matn,dest='uz').text
    else:
        return translator.translate(matn,dest='en').text

from translate import translate
import telebot

TOKEN="5031637338:AAEjm-3aovDtQdfb0B61TPQGBHxqIzYvEPA"
tarjimonbot=telebot.TeleBot(token=TOKEN)