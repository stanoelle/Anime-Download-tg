import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6201307785:AAG0gB_uqvs9_konxBuLouEH9fwvwIQdzsM')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello! I am a movie download bot. Just send me the name of the movie you want to download and I will provide direct download links.')

@bot.message_handler(func=lambda msg: msg.text is not None) 
def send_movie_links(message):
    movie_name = message.text
    sites = ['yts', 'eztv', 'rarbg']
    for site in sites:
        search_url = f'https://{site}.ag/search/{movie_name}/'
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links to torrent files or direct downloads
        links = soup.find_all('a', {'href': re.compile('.*\.(torrent|mp4|mkv)')}) 
        
        # Get first 5 links and send to user
        send_links = ''
        for i, link in enumerate(links):
            if i == 5: 
                break
            send_links += link.get('href') + '\n'
        if send_links:
            bot.reply_to(message, send_links)
            break
bot.infinity_polling()
