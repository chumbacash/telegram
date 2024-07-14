from telegram import Update, ReplyKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7416568716:AAGb3ne9CkPM9kYXI7PkV6NufS17okW-P8I'

# --- Menu Functions ---

async def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [
        ["💬 To Dm", "💬 To Groups"],
        ["❔ Help"]
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Choose an option:", reply_markup=markup)

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("This bot can send mass messages. Use the menu to choose an action.")

async def mass_message_dms(update: Update, context: CallbackContext) -> None:
    # Example user IDs - replace with actual user IDs
    users = [123456789, 987654321]  # Replace with your list of user IDs
    message = "Your message text here"
    for user_id in users:
        await context.bot.send_message(chat_id=user_id, text=message)
    await update.message.reply_text("Mass message sent to DMs.")

async def mass_message_groups(update: Update, context: CallbackContext) -> None:
    # Example group IDs - replace with actual group IDs
    groups = [-123456789, -987654321]  # Replace with your list of group IDs
    message = "Your message text here"
    for group_id in groups:
        await context.bot.send_message(chat_id=group_id, text=message)
    await update.message.reply_text("Mass message sent to groups.")

# Create the Application and pass it your bot's token.
application = Application.builder().token(BOT_TOKEN).build()

# --- Persistent Menu Setup ---

commands = [
    BotCommand("start", "Start the bot"),
    BotCommand("help", "Get help")
]
application.bot.set_my_commands(commands)

# --- Handlers ---

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(MessageHandler(filters.Regex('^Mass Message to DMs$'), mass_message_dms))
application.add_handler(MessageHandler(filters.Regex('^Mass Message to Groups$'), mass_message_groups))
application.add_handler(MessageHandler(filters.Regex('^Help$'), help_command))

# Start the Bot
if __name__ == '__main__':
    application.run_polling()
