from config         import OPTO_GROUP_ID, TAGS_PER_MESSAGE

from telegram       import Update
from telegram.ext   import Updater, CommandHandler, CallbackContext

class Bot():
    def __init__(self, api_key: str):
        # print(f"Hello world, my API key is: {api_key}")
        self.api_key = api_key

    def command_tag_all(update: Update, context: CallbackContext) -> None:
        # print(update["message"]["chat"]["id"])
        # print(OPTO_GROUP_ID)
        if str(update["message"]["chat"]["id"]) != str(OPTO_GROUP_ID):
            return

        administrators = context.bot.get_chat_administrators(chat_id=OPTO_GROUP_ID)
        
        user_list = []
        for admin in administrators:
            user_list.append((admin["user"]["id"], "@" + admin["user"]["username"] if admin["user"]["username"] else admin["user"]["first_name"]))

        # message = "\n".join([f"[{user[1]}](tg://user?id={user[0]}) " for user in user_list])
        iterations = 1 + (len(user_list) // TAGS_PER_MESSAGE)

        for i in range(iterations):
            message = "\n".join([f'<a href="tg://user?id={user[0]}">{user[1]}</a>' for user in user_list[i*TAGS_PER_MESSAGE:i*TAGS_PER_MESSAGE + TAGS_PER_MESSAGE]])
            print(message)
            context.bot.send_message(OPTO_GROUP_ID, message, parse_mode="html", disable_notification=False)

        

    def command_help(update: Update, context: CallbackContext) -> None:
        context.bot.send_message(OPTO_GROUP_ID, "Use o comando /tag_all para marcar todos os membros do grupo.")

    def start(self):
        print("Execution started...")

        # Creates bot wrapper
        updater = Updater(self.api_key)
        
        # Dispacher to register handlers
        dispatcher = updater.dispatcher

        # Bot commands
        dispatcher.add_handler(CommandHandler("tag_all",    Bot.command_tag_all))
        dispatcher.add_handler(CommandHandler("help",       Bot.command_help))

        
        # Start bot
        updater.start_polling()
        updater.idle()

