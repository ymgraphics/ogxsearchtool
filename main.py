import telebot
import requests

# Create a Telegram Bot object
bot = telebot.TeleBot("1837525814:AAEGfFv1rSm0EegY1M_xnxEAbf1UD-cv6eo")

# Handle the "/getopportunity" command
@bot.message_handler(commands=['getopportunity'])
def handle_get_opportunity(message):
    # Extract the search query and committee ID from the user's message
    query = message.text.split(' ', 1)[1]

    # Build the request URL using the provided API endpoint and access token
    url = "https://gis-api.aiesec.org/v2/opportunities?access_token={ACCESS_TOKEN}&api_key={API_KEY}"
    params = {
        "access_token": "09493ff6cd688cdeefcfe90ed39248488f0ef883b872cdf398e34c0b5d7914f9",
        "api_key": "09493ff6cd688cdeefcfe90ed39248488f0ef883b872cdf398e34c0b5d7914f9",
        "q": query,
    }

    # Send a GET request to the API and retrieve the response
    response = requests.get(url, params=params)
    
    # Extract the opportunities data from the response
    opportunities = response.json()["data"]
    
    # Build the message to send back to the user
    message_text = "Here are the available opportunities for {}: \n\n".format(query)
    for opportunity in opportunities:
        message_text += "Title: {}\n".format(opportunity["title"])
        message_text += "Link: {}\n".format(opportunity["url"])
        message_text += "Duration: {}\n".format(opportunity["duration"])
        message_text += "Location: {}\n".format(opportunity["location"])
        message_text += "Product: {}\n\n".format(opportunity["programmes"]["short_name"])
    
    # Send the message back to the user
    bot.send_message(message.chat.id, message_text)

# Start the bot
bot.polling()
