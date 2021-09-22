import pyttsx3 # to convert text data into speech using python
import datetime
import speech_recognition as sr  # convert speech to text
import smtplib # built in library to send mails
from important import sender,pwd 
from email.message import EmailMessage
import pyautogui
import webbrowser as web
from time import sleep
import time as tt
import keyboard 
import wikipedia
import pywhatkit
import requests
import clipboard
import os
import pyjokes
import string
import random
import psutil # library for cpu usage and battery etc..
from nltk.tokenize import word_tokenize

engine = pyttsx3.init()
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def voice(change):
    voices = engine.getProperty('voices')
    speak(f"Calling {change}")

    if change == "jarvis":
        engine.setProperty('voice',voices[0].id)
        speak("yes sir, How may I help You")
    elif change == "friday":
        engine.setProperty("voice",voices[1].id)
        speak("yes sir, How may I help You")

    

def time():
    cur_time= datetime.datetime.now().strftime("%I:%M:%S") # strf used to set time in given format , I=HOURS, M=minutes , S= seconds
    speak("Current time is:")
    speak(cur_time)

def getmonth(value):
    months = ["January","february","march","april","may","june","july","august","september","october", "november","december"]
    return months[value-1]


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("Today's date is:")
    speak(day)
    cur_mon = getmonth(month)
    speak(cur_mon)
    speak(year)

def wish():
    speak("welcome back sir")
    greating()
    speak("how may i help you")

def greating():
    hour = datetime.datetime.now().hour

    if hour>=4 and hour < 12:
        speak("Good morning")
    elif hour>=12 and hour <= 17:
        speak("Good afternoon")
    elif hour>=18 and hour<21:
        speak("Good evening")
    elif hour>=21 and hour<=23:
        speak("Good night")
    else:
        speak("it's midnight")        

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1 # take a pause for 1sec
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-IN") # using api from google to convert speech to text
        print(query)
    except Exception as e:
        print(e)
        speak("sorry, please can you say that again")
        takecommand()
    return query 

def sendEmail(receiver,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587) #gmail at 587 port no.
    server.starttls() # start transport layer security
    server.login(sender, pwd)
    email = EmailMessage()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwhatsappsingle(phone,msg):
    phone = "+91" + phone
    web.open('https://web.whatsapp.com/send?phone='+phone+'&text='+msg)
    sleep(15)
    pyautogui.press('enter')

def sendwhatsappgrp(grp_id,content):
    web.open("https://web.whatsapp.com/accept?code="+ grp_id)
    sleep(15)
    keyboard.write(content)
    sleep(1)
    pyautogui.press('enter')

def searchgoogle(search):
    web.open("https://www.google.com/search?q="+search)

# http://api.openweathermap.org/data/2.5/weather?q=Delhi,IN&units=imperial&appid=2abcd3c02d658c07dd37fb146c50c804

def news():

    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=8bc082852c06481abbe3a5cef1842872'

    data = requests.get(url).json()
    articles = data['articles']
    articles = articles[:5]

    for i in articles:
        title = i['title']
        description = i['description']
        print(title)
        print()
        print(description)
        speak(title)

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text) 

def covid():
    data = requests.get("https://coronavirus-19-api.herokuapp.com/all").json()

    covid_data = f'confirmed cases {data["cases"]} \n deaths {data["deaths"]} \n recovered {data["recovered"]}'   
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\Asus\\Desktop\\Jarvis\\screenshots\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def pwdgenerator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    pwdlen = 8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpwd = ("".join(s[0:pwdlen]))
    print(newpwd)
    speak(f"your new password is{newpwd}")
    speak(f"repeating your new password{newpwd}")

def flipcoin():
    speak("sure sir, choose one, heads or tails")
    choice = takecommand().lower()
    coin = ["heads","tails"]
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    print(toss)
    if choice==toss:
        speak(f"{toss} it is, You won")
    else:
        speak(f"{toss} it is, You lose, better luck next time")
    
def rolldie():
    speak("sure sir, rolling the die")
    die =["1","2","3","4","5","6"]
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    print(f"you got {roll}")
    speak(f"you got{roll}")

def cpu():
    usage = str(psutil.cpu_percent())
    speak(f"cpu usage is {usage}")
    battery =  psutil.sensors_battery() #list
    speak(f"Your system's battery percentage is {battery.percent} percent")

def closeApp(app):

    speak(f"closing {app}")

    if app == "chrome":
        os.system("TASKKILL /F /im chrome.exe")
        
    elif app == "code":
        os.system("TASKKILL /F /im Code.exe")


if __name__ == "__main__":
    hello = takecommand()
    wish()
    while True:
        command = takecommand().lower()
        command_tok = word_tokenize(command)
        #print(command_tok)

        if 'time' in command_tok:
            time()

        if 'date' in command_tok:
            date()   
        
        if 'call' in command_tok:
            to_call = command_tok
            to_call = to_call[-1:-2:-1]   
            voice(to_call[0])

        if 'mail' in command_tok:
            contacts = {
                'bhavya':"bhavyrastogi2002@gmail.com",
                'raghav':"Raghavkhanna0011@gmail.com",
                'anirudh':"osho.anirudh@gmail.com"
            }
            try:
                speak("to whom you want to send mail?")
                name = takecommand().lower()

                if name in contacts:
                    receiver = contacts[name]
                else:
                    speak("no contact found")
                    speak(name)
                    continue; 
                    
                speak("what is the subject of mail?")
                subject = takecommand()
                speak("what should I send")
                content = takecommand()
                sendEmail(receiver,subject,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Unable to send mail")
        
        if 'message' in command_tok:
            wap_contacts ={
                'mi': '9871150866',
                'apna it':'Jz2HXFh0XFKLVvj9BZ2Nxk'
            }
        
            try:
                speak("should i send to group or to a person")
                grporper = takecommand().lower()

                speak("to whom you want to send message?")
                name = takecommand().lower()

                if name in wap_contacts:
                    receiver = wap_contacts[name]
                else:
                    speak(f"no contact found {name}")
                    speak("do, u want to send message through mobile number")
                    choice = takecommand().lower()

                    if choice == "yes":
                        speak("tell me the number")
                        receiver = takecommand()
                    else:
                        continue; 

                speak("what should I say")
                content = takecommand()

                name = word_tokenize(receiver)
                speak("sending message to")
                speak(name)

                if grporper == 'person':
                    sendwhatsappsingle(receiver,content)
                else:
                    sendwhatsappgrp(receiver,content)

                speak("message has been sent")

            except Exception as e:
                print(e)
                speak("Unable to send message")

        if 'wikipedia' in command_tok:
            print("searching...")
            speak("searching")
            command = command.replace("search","")
            command = command.replace("jarvis","")
            command = command.replace("on","")
            command = command.replace("wikipedia","")
            result = wikipedia.summary(command,sentences = 3)
            print(result)
            speak(result)
        
        if 'google' in command_tok:
            command = command.replace("search","")
            command = command.replace("jarvis","")
            command = command.replace("on","")
            command = command.replace("google","")
            searchgoogle(command)
        
        if 'youtube' in command:
            speak("what should i play on youtube")
            topic = takecommand()
            pywhatkit.playonyt(topic)

        if 'weather' in command_tok:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi,IN&units=imperial&appid=2abcd3c02d658c07dd37fb146c50c804'

            data = requests.get(url).json()
            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            temp = round((temp-32) * 5/9)
            description = data['weather'][0]['description']
            print(weather)
            print(temp)
            print(description)
            speak(f'temperature is {temp} degree celcius')
            speak(f"it's {description} outside")

        if 'headlines' in command_tok:
            news()
            speak("that's all for today, have a nice day")
        
        if 'read' in command_tok:
            text2speech()
        
        if 'covid' in command_tok or 'corona' in command_tok:
            covid()

        if 'open vs code' in command:
            path = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        if 'chrome' in command_tok:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        
        if 'joke' in command_tok or 'jokes' in command_tok :
            speak(pyjokes.get_joke())
        
        if 'screenshot' in command_tok:
            screenshot()

        if 'remember this' in command:
            speak("what should i remember?")
            data = takecommand()
            data = data.replace("remember","")
            data = data.replace("that","")
            data = data.replace("I","You")
            speak("I successfully noted info")
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        
        if 'to remember' in command:
            remember = open("data.txt","r")
            speak("You told me to remember that"+ remember.read())
        
        if 'password' in command_tok:
            pwdgenerator()
        
        if 'flip' in command_tok:
            flipcoin()
        
        if 'roll' in command_tok:
            rolldie()
        
        if 'battery' in command_tok or 'cpu' in command_tok:
            cpu()
        
        if 'close' in command_tok:
            to_close = command_tok
            to_close = to_close[-1:-2:-1]
            closeApp(to_close[0])
            
        if 'offline' in command_tok:
            speak("Ok")
            break 

