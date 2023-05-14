import requests
import bs4

from telegram.ext import Updater, CommandHandler


# Define your bot token here
BOT_TOKEN = '6201307785:AAGZrQXOhM7m70Gcne4mTBuInrmc_Ta5dyY'


def anime_search(update, context):
    """Searches for anime and returns a download link."""
    query = ' '.join(context.args)
    url = "https://www.zoro.to/search?q=" + query
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", class_="col-sm-6 col-md-4 col-lg-3")
    for result in results:
        title = result.find("a", class_="title").text
        link = result.find("a", class_="title").get("href")
        context.bot.send_message(chat_id=update.effective_chat.id, text=title + " - " + link)


def start(update, context):
    """Sends a welcome message when the bot is started."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the anime download bot! Send me the name of an anime to get a download link.")


def main():
    """Starts the bot."""
    # Set up the bot and its handlers
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("anime", anime_search, pass_args=True))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
