import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Boss The current time is")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Boss today's date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Boss!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon ")
    elif hour>=18 and hour<24:
        speak("Good Evening")
    else:
        speak("Good Night boss Sleep well")
    speak("I am ready to help you Boss")
    speak("How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mokeshv.professional@gmail.com', 'mokesh@gmail.com')
    server.sendmail('230024.ec@rmkec.ac.in', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\Projects\Sample\venv\save.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)
    battery = psutil.sensors_battery()
    speak("Your battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wiki' in query:
            speak("Searching Boss!")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'mokeshvelraj123@gmail.com'
                sendemail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search' in query:
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'lock' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 0")

        elif 'restart' in query:
            os.system("shutdown /r /t -l")

        elif 'songs' in query:
            speak("Playing songs for you sir!")
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember' in query:
            speak("What should I remember sir?")
            data = takeCommand()
            speak("You said to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt' , 'r')
            speak("You told me that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("screenshot taken boss!")

        elif 'cpu usage' in query:
            cpu()
        
        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()
        