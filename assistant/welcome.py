from time_module import get_hours,get_date
from output_module import output
import  database
from datetime import date


def greet():

    #fetch todays date
    today_date = get_date()
    database.update_last_seen(today_date)

    #fetch previous date
    previous_date = database.get_last_seen()

    if previous_date == today_date:
        output("Welcome back ,Sir and i would be happy if Internet connection is available")

    else:

        hour = int(get_hours())

        if hour >= 4 and hour < 12 :
            output("Good Morning")

        elif hour>=12 and hour <16:
            output("Good Afternoon")

        else:
            output("Good Evening")
