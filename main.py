import telebot
from pyrogram import Client

# Initialize telebot instance
bot = telebot.TeleBot("6201307785:AAG0gB_uqvs9_konxBuLouEH9fwvwIQdzsM")

# Define the function to search for movies
def search_movies(query):
    with Client("BQAFUYDEHtMiZWocKu5762avgI1rUfRqEXdSRnCjItXqSpzDifoGSWhUwQG3XU8pElqA0muKkMSap7L4VIMlI3nneIEGm_woktY4z8u9ghKfNkBjUEaxwEoBUlTADaWfnJ_QT9JV1zrUSJ2Vb0035JI7xifKPD7faa1o-EJSI5lT5KR-QVijaaTXYVoV-1d3RDchKhAp7xUENuT22Yn4e0Uy5mofftxWPzpiFVoHKmmZy17f8Jxtg_sgVFsQZBBV0_RXzUf2HKvX9Ri2BEa9P11iuF_xClfe-d_g7tBHiTjhqIgbhg3ja4SI3rZ48ClzT21sLa1lPrf8dwwUIg1JNQqPAAAAAXauqbEA", api_id=26331302, api_hash='5d7bbff0c04b119735e4e14bdb402e69') as app:
        # Join the channel
        app.join_chat("moviessfreeee")
        # Search for movies in the channel
        messages = app.get_chat_history("moviessfreeee", filter='video', limit=10)
        for message in messages:
            if query.lower() in message.caption.lower():
                # Return the file URL
                return message.video.file_id
    return None

# Define the '/start' command handler
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Welcome! You can search for movies using the '/search' command.")

# Define the '/search' command handler
@bot.message_handler(commands=['search'])
def search_command(message):
    query = message.text.split('/search', maxsplit=1)[1].strip()
    file_id = search_movies(query)
    if file_id:
        bot.send_message(message.chat.id, f"Here is the movie: {file_id}")
    else:
        bot.send_message(message.chat.id, "Movie not found.")

# Run the bot
bot.polling()
