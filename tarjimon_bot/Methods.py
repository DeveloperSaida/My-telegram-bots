def start(update,context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,text=f"Salom @{user.first_name} bizning telegram botimizga xush kelibsiz!")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bu bot o`zbek-turk tili tarjimon boti ,"
                             "marhamat matnni kirirting...")