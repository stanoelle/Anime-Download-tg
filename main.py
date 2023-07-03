import telebot
from pyrogram import Client

bot = telebot.TeleBot('5d7bbff0c04b119735e4e14bdb402e69')
client = Client("BQAFUYDEHtMiZWocKu5762avgI1rUfRqEXdSRnCjItXqSpzDifoGSWhUwQG3XU8pElqA0muKkMSap7L4VIMlI3nneIEGm_woktY4z8u9ghKfNkBjUEaxwEoBUlTADaWfnJ_QT9JV1zrUSJ2Vb0035JI7xifKPD7faa1o-EJSI5lT5KR-QVijaaTXYVoV-1d3RDchKhAp7xUENuT22Yn4e0Uy5mofftxWPzpiFVoHKmmZy17f8Jxtg_sgVFsQZBBV0_RXzUf2HKvX9Ri2BEa9P11iuF_xClfe-d_g7tBHiTjhqIgbhg3ja4SI3rZ48ClzT21sLa1lPrf8dwwUIg1JNQqPAAAAAXauqbEA")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your movie bot. You can search for movies by typing /search followed by the movie name.")
@bot.message_handler(commands=['search'])
def search_movie(message):
    movie_name = ' '.join(message.text.split()[1:])
    with client:
        for dialog in client.iter_dialogs():
            if dialog.chat.username == 'moviessfreeee':
                for message in client.search_messages(dialog.chat.id, query=movie_name):
                    bot.send_document(message.chat.id, message.document.file_id)

bot.polling()
