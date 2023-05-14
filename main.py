import requests
from bs4 import BeautifulSoup

from telegram import Update, Dispatcher, CommandHandler


def get_anime_link(anime_name):
  """Gets the download link for an anime from Zoro.to."""
  url = f"https://www.zoro.to/search?q={anime_name}"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  links = soup.find_all("a", class_="btn btn-success btn-block")
  return links[0]["href"]


def start(update: Update, context: Dispatcher):
  """Sends a welcome message to the user."""
  update.message.reply_text("Welcome to the anime bot! You can search for anime by typing /search <anime_name>.")


def search(update: Update, context: Dispatcher):
  """Searches for an anime and sends the download link to the user."""
  anime_name = update.message.text.split()[1]
  link = get_anime_link(anime_name)
  update.message.reply_text(link)


if __name__ == "__main__":
  # Create the updater and dispatcher
  updater = Updater("6201307785:AAGZrQXOhM7m70Gcne4mTBuInrmc_Ta5dyY")
  dispatcher = updater.dispatcher

  # Add the handlers
  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("search", search))

  # Start the bot
  updater.start_polling()
  updater.idle()
