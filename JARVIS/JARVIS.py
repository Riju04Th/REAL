import pyttsx3
# import speech_recognition as sr
import datetime
import os
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")
# def takeCommand():
# #It takes microphone input from the user and returns string output
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.adjust_for_ambient_noise(source)
#         r.pause_threshold = 0.5
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
    #     return None
    # return query
if __name__ == "__main__":
    Greetings()
    query = input("enter command: ")
    while True:
        if query == "play_music":
            music_dir = 'C:\\Users\\SUBHASISH ADDYA\\Desktop\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            print("Playing music")
