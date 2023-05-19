import telegram
import subprocess

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

def execute_code(update, context):
    # Extract the received message
    message = update.message.text

    # Execute the Python code
    result = subprocess.run(['python3', '-c', message], capture_output=True, text=True)

    # Send the output back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=result.stdout)

def main():
    # Create the updater and dispatcher
    updater = telegram.Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # Register the handler for executing code
    dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.text, execute_code))

    # Start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()
