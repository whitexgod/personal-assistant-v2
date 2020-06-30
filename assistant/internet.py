import socket
import wikipedia
import requests,webbrowser
import bs4

def check_internet_connection():

    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        return False
    else:
        return True


def check_on_wiki(query):

    query = query.lower()
    query = query.replace("who is","")
    query = query.replace("what is","")
    query = query.replace("do you know","")
    query = query.replace("tell me about", "")
    query = query.replace("tell me who is", "")
    query = query.replace("tell me what is", "")

    query = query.strip()

    try :
        data = wikipedia.summary(query, sentences=2)
        return data

    except Exception as e:
        return ""


def from_internet(query):

    query = query.lower()
    query = query.replace("who is", "")
    query = query.replace("what is", "")
    query = query.replace("do you know", "")
    query = query.replace("tell me about", "")
    query = query.replace("tell me who is", "")
    query = query.replace("tell me what is", "")

    query = query.strip()
    try:

        user_input = query
        print("Googling...")
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        res = requests.get("https://www.google.com/search?q=" + user_input, headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        tags = soup.find_all(name='div', class_='r')
        urls = []
        for i in range(5):
            urls.append(tags[i].find(name='a').attrs['href'])
        for j in urls:
            webbrowser.open(j)

        return "Opening the search results into your browser."

    except :

        return "Sorry sir, i still need to upgrade my modules!"
