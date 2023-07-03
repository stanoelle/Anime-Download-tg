import telebot
import pyrogram

# Create a pyrogram session
session = pyrogram.Client(
    "BQAFUYDEHtMiZWocKu5762avgI1rUfRqEXdSRnCjItXqSpzDifoGSWhUwQG3XU8pElqA0muKkMSap7L4VIMlI3nneIEGm_woktY4z8u9ghKfNkBjUEaxwEoBUlTADaWfnJ_QT9JV1zrUSJ2Vb0035JI7xifKPD7faa1o-EJSI5lT5KR-QVijaaTXYVoV-1d3RDchKhAp7xUENuT22Yn4e0Uy5mofftxWPzpiFVoHKmmZy17f8Jxtg_sgVFsQZBBV0_RXzUf2HKvX9Ri2BEa9P11iuF_xClfe-d_g7tBHiTjhqIgbhg3ja4SI3rZ48ClzT21sLa1lPrf8dwwUIg1JNQqPAAAAAXauqbEA",
    api_id=26331302,
    api_hash="5d7bbff0c04b119735e4e14bdb402e69",
)

# Create a Telegram bot
bot = telebot.TeleBot("6201307785:AAG0gB_uqvs9_konxBuLouEH9fwvwIQdzsM") 

# Define a function to search for movies
def search_movies(query):
    chat_id = message.chat.id
    channel = session.get_chat("https://t.me/moviessfreeee")
    messages = channel.get_messages(filter=channel.search(query))
    for message in messages:
        file_id = message.document.file_id
        file = session.download_file(file_id)
        bot.send_document(chat_id, file)

# Register a message handler for the /search command
@bot.message_handler(commands=["search"])
def handle_search_command(message):
    query = message.text.split(" ")[1]
    search_movies(query)

# Start the bot
bot.polling()
