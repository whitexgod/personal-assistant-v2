from output_module import output
from time_module import get_time,get_date
from input_module import take_input,take_command
from database import *
from internet import check_internet_connection,check_on_wiki,from_internet
from web import *
from quit import quit
import assistant_details
from movie_recommendation_module import movie_recommendation
from price_predictor import *

def process(query):

    if 'hi' in query :
        return "hello, Sir"
    elif 'hello' in query:
        return "Hi, Sir"
    elif "how are you" in query:
        return "I am fine sir, How are you doing?"
    elif "fine" in query:
        return "okay. What can i do for you sir."
    elif "thanks" in query:
        return "welcome, Sir"
    elif "thank you" in query:
        return "welcome, Sir"
    elif "sorry" in query:
        return "its ok, i never mind"
    elif "ok" in query:
        return "its nice to talk with you, Sir"
    elif "okay" in query:
        return "its nice to talk with you, Sir"
    elif "play music" in query:
        play_misic()
        return "playing music in youtube"
    elif "good morning" in query:
        return "Good Morning, Sir"
    elif "good evening" in query:
        return "Good evening, Sir"
    elif "good afternoon" in query:
        return "Good afternoon, Sir"
    elif "good night" in query:
        output("Good night, Sir")
        quit()
        #return "Good night, Sir"
    elif "open facebook" in query:
        open_facebook()
    elif "open my cv" in query:
        open_cv()
        return "opening your cv now"
    elif "open my google cv" in query:
        open_google_cv()
        return "opening your google cv now"
    elif "open my selling app" in query:
        open_my_selling_app()
        return "opening your selling app now in the browser"
    elif "open simon game" in query:
        open_simon_game()
        return "opening simon game in your browser"
    elif "open movie sentiment app" in query:
        open_my_movie_sentiment_app()
        return "opening movie sentiment app in your browser"
    elif "open movie recommender app" in query:
        open_my_movie_recommend_app()
        return "opening movie recommendation app in your browser"

    elif "search in wikipedia" in query:
        output("say what to search for in wikipedia")
        ans = take_input()
        ans.lower()
        answer = check_on_wiki(ans)
        if answer != "":
            return answer

    elif "search in internet" in query:
        output("say what to search for in internet")
        ans = take_input()
        ans.lower()
        answer = from_internet(ans)
        if answer != "":
            return answer

    elif "recommend me movies" in query:
        movie_recommendation()
        return "Sir, i hope you will like my recommendations."
    elif "recommend me movies again" in query:
        movie_recommendation()
        return "Sir, i hope you will like my recommendations."

    elif "open my github" in query:
        open_my_github()
        return "opening your github account sir"

    elif "open campusx page" in query:
        open_campusx()
        return "opening campusx official page in your browser"

    elif "open github" in query:
        open_github()
        return "opening github in browser"

    elif "activate price predictor module" in query:
        output("activating price predictor module")
        output("what do you want to sell?")
        output("options - mobile or bike or laptop/desktop or car or something else?")
        ans=take_command()
        if ans.lower()=="car":
            predict_car()
            return "I Hope the information would be helpful"
        elif ans.lower()=="mobile":
            predict_mobile()
            return "I Hope the information would be helpful"
        elif ans.lower()=="bike":
            predict_bike()
            return "I Hope the information would be helpful"
        elif ans.lower()=="laptop/desktop":
            predict_laptop()
            return "I Hope the information would be helpful"
        else:
            return (f"sorry, my maker is lazy hence i am still learning how to predict the price of {ans}")

    elif "activate price predictor module again" in query:
        output("activating price predictor module")
        output("what do you want to sell?")
        ans=take_command()
        if ans.lower()=="car":
            predict_car()
            return "I Hope the information would be helpful"
        elif ans.lower()=="mobile":
            predict_mobile()
            return "I Hope the information would be helpful"
        elif ans.lower()=="bike":
            predict_bike()
            return "I Hope the information would be helpful"
        elif ans.lower()=="laptop/desktop":
            predict_laptop()
            return "I Hope the information would be helpful"
        else:
            return (f"sorry, my maker is lazy hence i am still learning how to predict the price of {ans}")



    else:

        answer = get_answer_from_memory(query)

        if answer == "get time details" :
            return ("Time is "+ get_time())

        elif answer == 'quit':
            return ("Good-bye, Sir"+quit())

        elif answer== "check internet connection":
            if check_internet_connection():
                return "Internet is Connected"
            else:
                return "Internet is not Connected"

        elif answer == "tell date":
            return "Date is "+ get_date()

        elif answer == "on speak" :
            return turn_on_speech()

        elif answer == "off speak":
            return turn_off_speech()

        elif answer == "open facebook":
            open_facebook()
            return "opening facebook now"

        elif answer == "open google":
            open_google()
            return "opening google now"

        elif answer == "open browser":
            open_google()
            return "opening browser now"

        elif answer == "close browser":
            close_browser()
            return "Browser closed."

        elif answer == "change name":
            output("Okay! what do you want call me?")
            temp = take_command()
            if temp == assistant_details.name:
                return "Can't change. Its just my previous name"
            else:
                update_name(temp)
                assistant_details.name=temp
                return ("Now you can call me " + temp)

        else:

                return "Say that again please!"
