import telebot
import requests
from bs4 import BeautifulSoup

# Create a new Telegram bot
bot = telebot.TeleBot('6201307785:AAG0gB_uqvs9_konxBuLouEH9fwvwIQdzsM')

# Define the command to search for movies
@bot.message_handler(commands=['search'])
def search(message):
    # Get the movie title from the user's message
    title = message.text.replace('/search ', '')

    # Search for the movie on the download website
    response = requests.get(f'https://yts.mx/browse-movies/{title}/all/all/0/latest')
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_links = soup.find_all('a', {'class': 'browse-movie-title'})

    # If there are no search results, let the user know
    if not movie_links:
        bot.reply_to(message, 'Sorry, no results found. Please try again with a different search term.')
        return

    # Otherwise, send the user the first movie's download link
    movie_link = movie_links[0]['href']
    bot.reply_to(message, f'Here is the download link for {title}: {movie_link}')

# Start the bot
bot.polling()
