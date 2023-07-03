import telebot
from pyrogram import Client
from pyrogram.errors import UserNotParticipant, ChatAdminRequired

# Telegram Bot token
TOKEN = '6201307785:AAG0gB_uqvs9_konxBuLouEH9fwvwIQdzsM'

# Pyrogram session configuration
API_ID = 26331302
API_HASH = '5d7bbff0c04b119735e4e14bdb402e69'
SESSION_NAME = '..'
# Replace 'movie_channel' with the name or ID of your movie channel
movie_channel = '-1001927205991'


# Create a Pyrogram client
pyro_client = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# Create a Telebot instance
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Welcome to the Movie Search Bot! Send me the name of a movie to search for.')

@bot.message_handler(func=lambda message: True)
def search_movie(message):
    # Get the movie name from the user's message
    movie_name = message.text

    try:
        # Use the Pyrogram session to search for movies in the channel
        with pyro_client:
            # Join the channel where you have the movies
            pyro_client.join_chat(movie_channel)

            # Search for the movie in the channel
            results = pyro_client.search_messages(movie_channel, movie_name)

            # Check if any results were found
            if results.total > 0:
                # Get the first result
                first_result = results[0]

                # Check if the result is a document (file)
                if first_result.document:
                    # Send the file to the user
                    bot.send_document(message.chat.id, first_result.document.file_id)
                else:
                    bot.reply_to(message, 'No movie file found.')
            else:
                bot.reply_to(message, 'No movie found.')

    except UserNotParticipant:
        bot.reply_to(message, 'Please join the movie channel to search for movies.')

    except ChatAdminRequired:
        bot.reply_to(message, 'I need admin access to search for movies in the channel.')

# Start the bot
bot.polling()
