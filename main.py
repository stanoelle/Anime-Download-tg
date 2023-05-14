import requests
import bs4

from telegram.ext import Updater, CommandHandler

# Get your API ID and API hash from https://api.telegram.org/botfather
API_ID = 7211896
API_HASH = 'd22a4d25860c6673209ea07dc194857a'

# Get your bot token from https://t.me/botfather
BOT_TOKEN = '6201307785:AAGZrQXOhM7m70Gcne4mTBuInrmc_Ta5dyY'

# Create the updater
updater = Updater(token=BOT_TOKEN, use_context=True)

# Define a command handler for the /search command
@updater.command(command='search')
def search(update, context):
    # Get the anime name from the user
    query = update.message.text

    # Scrape the download links from 9anime.to
    url = 'https://9anime.to/search?q=' + query
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find the download links
    download_links = soup.find_all('a', class_='btn btn-success btn-sm')

    # Send the download links to the user
    for download_link in download_links:
        context.bot.send_message(chat_id=update.effective_chat.id, text=download_link['href'])

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl+C
updater.idle()
