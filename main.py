import telebot

from pyrogram import Client, filters

import re



# Set up the telebot and Pyrogram session

bot_token = '6201307785:AAG0gB_uqvs9_konxBuLouEH9fwvwIQdzsM'

bot = telebot.TeleBot(bot_token)

api_id = '26331302'

api_hash = '5d7bbff0c04b119735e4e14bdb402e69'

pyrogram_session = 'BQAFUYDEHtMiZWocKu5762avgI1rUfRqEXdSRnCjItXqSpzDifoGSWhUwQG3XU8pElqA0muKkMSap7L4VIMlI3nneIEGm_woktY4z8u9ghKfNkBjUEaxwEoBUlTADaWfnJ_QT9JV1zrUSJ2Vb0035JI7xifKPD7faa1o-EJSI5lT5KR-QVijaaTXYVoV-1d3RDchKhAp7xUENuT22Yn4e0Uy5mofftxWPzpiFVoHKmmZy17f8Jxtg_sgVFsQZBBV0_RXzUf2HKvX9Ri2BEa9P11iuF_xClfe-d_g7tBHiTjhqIgbhg3ja4SI3rZ48ClzT21sLa1lPrf8dwwUIg1JNQqPAAAAAXauqbEA'



# Start the Pyrogram Client

app = Client(pyrogram_session, api_id=api_id, api_hash=api_hash)

app.start()



# Define the movie search function



# Start the Pyrogram Client
# Define the movie search function
@bot.message_handler(commands=['movie'])
def search_movies(message):
    # Get the movie name from the user
    movie_name = message.text.replace('/movie ', '')

    # Search for movies in the channel https://t.me/moviessfreeee
    messages = app.search_messages('moviessfreeee', movie_name, filter='document')

    # If a file is found, send it to the user
    found = False
    for message in messages:
        for doc in message.document:
            if doc.mime_type == "video/mp4":
                bot.send_document(message.chat.id, message.document.file_id)
                found = True
                break
        if found:
            break
    if not found:
        bot.reply_to(message, "No movies found. Please try again.")

# Start the telebot
bot.polling()



# Start the telebot

bot.polling()

