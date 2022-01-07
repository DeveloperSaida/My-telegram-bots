from gtts import gTTS
def start(update,context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,text=f"Salom @{user.first_name} bizning telegram botimizga xush kelibsiz!")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bu bot ingliz tilidagi matnni audioga aylantirib beradi,"
                             "marhamat matnni kirirting...")

def text_to_audio(matn):
    speach=gTTS(text=matn)
    speach.save('audios/mars17_30.mp3')
    audio=open("audios/mars17_30.mp3",'rb')
    return audio

def xabar(update,context):
    matn=update.message.text
    context.bot.send_audio(chat_id=update.effective_chat.id,audio=text_to_audio(matn))
