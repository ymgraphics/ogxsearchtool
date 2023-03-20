import telebot
import requests

# Create a Telegram Bot object
bot = telebot.TeleBot("5834472319:AAG9YhDqBJwbp4tWhLfrlGQlS_zuEQaW2KM")

# Handle the "/getopportunity" command
@bot.message_handler(commands=['getopportunity'])
def handle_get_opportunity(message):
    try:
        query, country_filter = message.text.split(' ', 2)[1:]
    except ValueError:
        bot.reply_to(message, "Please enter a search query and a country filter in the format /getopportunity <query> in <country>")
        return
    
    # Build the request URL to retrieve the committee ID
    committee_url = "https://gis-api.aiesec.org/v2/committees/autocomplete"
    committee_params = {
        "access_token": "09493ff6cd688cdeefcfe90ed39248488f0ef883b872cdf398e34c0b5d7914f9",
        "q": country_filter
    }
    
    # Send a GET request to retrieve the committee ID
    committee_response = requests.get(committee_url, params=committee_params)
    committee_data = committee_response.json()
    
    # Extract the committee ID from the response
    committee_id = None
    if committee_data and 'data' in committee_data and len(committee_data['data']) > 0:
        committee_id = committee_data['data'][0]['id']
    
    # Build the request URL using the provided API endpoint and access token
    url = "https://gis-api.aiesec.org/v2/opportunities"
    params = {
        "access_token": "09493ff6cd688cdeefcfe90ed39248488f0ef883b872cdf398e34c0b5d7914f9",
        "q": query,
        "api_key": "09493ff6cd688cdeefcfe90ed39248488f0ef883b872cdf398e34c0b5d7914f9"
    }

    if committee_id:
        params["filters[committee]"] = committee_id
    else:
        bot.reply_to(message, "Invalid country filter. Please try again.")
        return
    
    # Send a GET request to the API and retrieve the response
    response = requests.get(url, params=params)
    data = response.json()
    if 'data' not in data:
        bot.reply_to(message, "No opportunities found for the provided search query and country filter.")
        return

    # Extract the opportunities data from the response
    opportunities = data["data"]

    if data["data"]:
        opportunities = data["data"]
        message_text = f"Opportunities for '{query}'"
        if country_filter:
            message_text += f" in {country_filter}"
        message_text += ": \n\n"
        
        for opportunity in opportunities:
            message_text += f"{opportunity['title']} - {opportunity['url']}\n"
            message_text += "Title: {}\n".format(opportunity["title"])
            message_text += "Link: {}\n".format(opportunity["url"])
            message_text += "Duration: {}\n".format(opportunity["duration"])
            message_text += "Location: {}\n".format(opportunity["location"])
            message_text += "Product: {}\n\n".format(opportunity["programmes"]["short_name"])
    
    # Send the message back to the user
    bot.send_message(message.chat.id, message_text)

# Start the bot
bot.polling()


#f""