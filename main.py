import requests

import bs4

from telegram.ext import Updater, CommandHandler

def anime_search(bot, update, args):

    """Searches for anime and returns a download link."""

    query = args[0]

    url = "https://www.zoro.to/search?q=" + query

    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.content, "html.parser")

    results = soup.find_all("div", class_="col-sm-6 col-md-4 col-lg-3")

    for result in results:

        title = result.find("a", class_="title").text

        link = result.find("a", class_="title").get("href")

        bot.send_message(update.message.chat_id, title + " - " + link)

def start(bot, update):

    """Sends a welcome message when the bot is started."""

    bot.send_message(update.message.chat_id, "Welcome to the anime download bot! Send me the name of an anime to get a download link.")

def main():

    """Starts the bot."""

    updater = Updater("6201307785:AAGZrQXOhM7m70Gcne4mTBuInrmc_Ta5dyY")

    updater.dispatcher.add_handler(CommandHandler("start", start))

    updater.dispatcher.add_handler(CommandHandler("anime", anime_search))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":

    main()

