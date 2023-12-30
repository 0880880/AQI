from datetime import datetime

import aqi
import telebot


TOKEN = "<TOKEN>"

bot = telebot.TeleBot(TOKEN)

current_aqi = aqi.get_aqi()

last_update_time = datetime.now()

def check_update():
    global last_update_time
    current_time = datetime.now()
    time_difference = current_time - last_update_time

    if time_difference.total_seconds() >= 600:
        current_aqi = aqi.get_aqi()

        last_update_time = datetime.now()

@bot.message_handler(commands=['aqi', 'airquality'])
def send_aqi(message):
    check_update()
    bot.reply_to(message, "Current Tehrain air quality (PM2.5) : " + str(current_aqi))

@bot.message_handler(commands=['tatil'])
def is_closed(message):
    check_update()
    ans = "Na"
    if current_aqi > 150: ans = "Are"
    bot.reply_to(message, "Aya madares tatil hastan?2?22?\n\n" + ans + " (" + str(current_aqi) + "PM2.5)")


if __name__ == "__main__":
    bot.infinity_polling()
