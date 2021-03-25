import requests
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spvoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("news for today")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=e20a4e7d676e47f2b53f148896539268"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["status"])
    print(news_dict["totalResults"])
    art = news_dict["articles"]
    for article in art:
        speak(article["title"])
        time.sleep(1)
        speak("next news")
        speak("that's all about today news thanks for listening")