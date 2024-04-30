import pyttsx3
import datetime
import os
import pyaudio
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am Jarvis Sir. Please tell me how may I help you")       
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google_cloud(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        if 'play_music' in query:
            music_dir = 'C:\\Users\\SUBHASISH ADDYA\\Desktop\\My Python\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            print("Playing music")
