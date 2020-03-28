import speech_recognition as sr
from gtts import gTTS
import playsound
import time
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
from googlesearch import search


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("good morning")
        print("good morning")
    elif hour >=12 and hour <18 :
        speak("good afternoon")
        print("good afternoon")
    else:
        speak("good evening")
    speak("i am zira")

def takeCommand():#it takes input from the user and return  string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.... wait karo ")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said :{query}\n")
    except Exception as e:
        print(e)
        print("say again please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lovesat8181@gmail.com','Satish@8181')
    server.sendmail('lovesat8181@gmail.com' , to , content)
    server.close()

def search():
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
    speak("what are you want to search")
    query = takeCommand()
    for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
        print(j)
    webbrowser.open(j)
    speak("your"+ query +"is opened")
    

if __name__ == "__main__":
    wishMe()
    a = 1
    while (a <= 2):
        query = takeCommand().lower()
        # our taks

        if 'wikipedia' in query:
            speak("searching")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("according to wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            search()
        elif 'close google' in query:
            os.system("taskkill /im iexplore.exe /f")
        elif 'play music' in query:
            music_dir = 'E:\\satish music collection'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f" sir the  is  {strTime}")
        elif "open code" in query:
            codepath = "C:\\Users\\Ram\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = 'lovesat8181@gmail.com'
                sendEmail(to,content)
                speak("email has been sended")
            except Exception as e:
                print(e)
                speak("sorry dear email is not send please try angain")
        elif 'open notepad' in query:
            os.startfile('notepad.exe')
        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")
        elif 'close music' in query:
            os.system("taskkill /f /im wmplayer.exe " )
        elif "close code" in query:
            os.system("taskkill / f/ im code.exe") 
        elif "make a folder" in query:
            speak("folder name please")
            NameOfFolder = takeCommand().lower()
            try:
                os.mkdir(NameOfFolder)
                print("folder" , NameOfFolder ,  "is Created ") 
            except FileExistsError:
                print("folder " , NameOfFolder ,  " is already exists")
        elif "delete a folder" in query:
            speak("folder name please")
            NameOfFolder1 = takeCommand().lower()
            try:
                os.rmdir(NameOfFolder1)
                print("folder" , NameOfFolder1 ,  "is deleted ") 
            except FileExistsError:
                print("folder " , NameOfFolder1 ,  " is not exists")  
        a = a+1










'''
def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said =""

        try:
            said = r.recognize_google(audio)       
        except Exception as e:
            print("exception :",str(e))
    return said
speak("arpit is the good boy")'''