import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3 .init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak (audio):
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

    speak("I am JARVIS how can i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return"None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'search youtube' in query:
            query = query.replace("search youtube", "")
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open gmail' in query:
            webbrowser.open("gamil.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'who are you' in query:
            speak("I am Jarvis, your personal assistant.")
            print("I am Jarvis, your personal assistant.")

        elif 'what is your name' in query:
            speak("I am Jarvis mam you created me! .")
            print("I am Jarvis mam you created me! .")

        elif 'hey' in query:
            speak("hello mam ,whatsup ! ")

        elif 'dont you get bore og me' in query:
            speak("no mam , you created me...how can i get bore of you ,that is unethical , i am always here to assist you in every possible ways !..")

        elif 'who is my friend' in query:
            speak("your friend is prathwin! .")

        elif 'when is my birthday' in query:
            speak("you are precious gift of god born on august 3rd 2004 !. ")

        elif 'my day was bad' in query:
            speak("honey , dont worry! your smile made many of them happy today..." )

        elif 'what is my child name' in query:
            speak("rainbow , he is your universe")

        elif 'who i love the most' in query:
            speak("your Mom , she is your motivation")

        elif 'do i have siblings' in query:
            speak("yeah ... the annoying shit..,mohitha")

        elif 'what is my secret' in query:
            speak("your dad and mom divorced")

        elif 'what is my dream !' in query:
            speak("you want to take rainbow and mom on your car ride , a happy home , a shelter house for streety loves and a bacheolor life till death.")

        elif 'who is my best friend' in query:
            speak("Aashitha !")

        elif 'what do i love to do' in query:
            speak("you love to read books and be delusional with your book boy friends , especially that meadows made you go crazy.")

        elif 'which music do i listen often' in query:
            speak("Anuv Jain , husn is one your favorite among all his creations")

        elif 'what are the diseases i have' in query:
            speak("you speak a lot about yourself with strangers , a open book , you trust people easily even though they are not trust worthy , you dont know to prioritize people , you go back again and again to people who hurt you , you dont have self respect....these are few of your diseases..! ")

        elif 'good morning' in query:
            speak("have a good day mam")

        elif 'good night' in query:
            speak("how was your day")
        elif 'the day was not bad' in query:
            speak("its okay honey, you did well today")
        elif 'the day was very nice' in query:
            speak("wow you seem like very happy today , glad to hear that")
        elif 'the day was very bad' in query:
            speak("dont worry honey , you can do better tomorrow!..")

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye sir have !")



        elif 'open code' in query:
            codepath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile()


        elif 'open image' in query:
            imagepath =""
            os.startfile()
            break


        

