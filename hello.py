
from datetime import date
from datetime import datetime
import webbrowser
import pyttsx3

def talk( value):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(value)
    engine.runAndWait()

talk("My Name Is Jarvis! How Can I help You?")
while True:
    askme=(input("enter your query\n")).lower()
    talk("got your query")
    if askme==("open google").lower():
        talk("opening google")
        print("opening Google......")
        talk("you want to search for something?\n")
        askg=input("search something?(y/n)").lower()
        if askg==("y").lower():
            query=(input("enter what you want to search for\n")).lower()
            talk("searching for"+query)
            webbrowser.open_new_tab("https://www.google.com/search?q="+query)
        else:
            webbrowser.open_new_tab("https://www.google.com/")
    elif askme==("open website"):
        talk("enter the name of your website")
        ask1=(input("name of the website")).lower()
        ask2=(input("enter the extention of your website(.com,.in,etc)")).lower()
        talk("looking for"+ask1+ask2)
        url = "https://"+ask1+ask2
        webbrowser.open(url)
    elif askme==("open youtube").lower():
        talk("opening youtube")
        print("opening Youtube........")
        talk("you want to search for something?")
        askyt=input("search something?(y/n)").lower()
        if askyt==("y").lower():
            query=(input("enter what you want to search for\n")).lower()
            talk("searching for"+query)
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+query)
        else:
            webbrowser.open_new_tab("https://www.youtube.com/")
    elif askme==("time").lower():
        talk("the time is")
        print("fetching time............")
        today= datetime.now()
        d1 = today.strftime("%H:%M:%S")
        talk(d1)
        print(d1)