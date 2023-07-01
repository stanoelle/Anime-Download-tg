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

    # Send a GET request to the download website's search page
    url = f'https://yts.mx/browse-movies/{title}/all/all/0/latest'
    response = requests.get(url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the download link for the first search result
    download_links = soup.select('.download-torrent > a[href^="magnet"]')
    if not download_links:
        bot.reply_to(message, f"Sorry, no results found for '{title}'. Please try again with a different search term.")
        return

    magnet_link = download_links[0]['href']
    bot.reply_to(message, f"Here's the magnet link for '{title}': {magnet_link}")

# Start the bot
bot.polling()
# Start the bot
bot.polling()
