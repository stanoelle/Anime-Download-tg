import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello! I am a movie download bot. Just send me the name of the movie you want to download and I will provide direct download links.')

@bot.message_handler(func=lambda msg: msg.text is not None) 
def send_movie_links(message):
    movie_name = message.text
    search_queries = [
        f'index of {movie_name} mkv',
        f'index of {movie_name} mp4'
    ]
    for query in search_queries:
        response = requests.get(f'https://google.com/search?q={query}')
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        send_links = ''
        for link in links:
            if any(name in link.get('href') for name in ['mp4', 'mkv']):
                send_links += link.get('href') + '\n'
        if send_links:
            bot.reply_to(message, send_links)
            break
bot.infinity_polling()
