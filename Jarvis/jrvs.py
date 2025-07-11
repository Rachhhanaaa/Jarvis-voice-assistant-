import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyjokes
import randfacts
import requests
 
from news import*
from yt_auto import music
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

API_KEY = "7b166e3269e21165f846b74a1124bf50"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

feelings = [
    "happy",
    "curious",
    "excited",
    "calm",
    "thoughtful"
]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning! I am JARVIS how can i help you?")

    elif hour>12 and hour<18:
        speak("good Afternoon mam! I am JARVIS how can i help you? ")

    else:
        speak("good evening mam ! I am JARVIS how can i help you?")
    
def playMusic(query):
    speak(f"Searching for {query} on YouTube...")
    music(query)  # Call the music function from YT_auto to play the song
    
# Function to get and speak the latest news
def tellNews():
    news = get_news()  # Call the function from News.py
    speak("Here are the top headlines:")
    speak(news) 
    print(news) # Read out the news
        
    

def takeCommand():
    # it takes microph input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please...")
        return "None"
    return query


def getWeather(city):
    # Function to get weather data
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        # Extract main weather information
        main = data["main"]
        weather = data["weather"][0]
        description = weather["description"]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]

        weather_report = f"The temperature in {city} is {temp}°C with {description}. The pressure is {pressure} hPa and the humidity is {humidity}%."
        return weather_report
    else:
        return "City not found."
    
def greet():
    greetings = [
        "Hello! how can i assist you today?",
        "Hi there! what can i do for you?",
        "Hey! need help with something?",
    ]
    speak(random.choice(greetings))

def express_feelings():
    current_feeling = random.choice(feelings)
    speak(f"I am feeling {current_feeling}today! how about you?")


def analyzeSentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score

def respondToSentiment(sentiment_score):
    #responds based on sentiment score
    if sentiment_score['compound'] >= 0.05:
        return "you seem sad today!"
    elif sentiment_score['compound'] <= -0.05:
        return "you seem a bit down today. is everything okay?"
    
        

def openSettings():
    # Open Windows settings
    speak("Opening system settings...")
    os.system("start ms-settings:")


def playSpotify(query):
    # Function to search and play songs on Spotify
    speak(f"Searching for {query} on Spotify...")
    query = query.replace("play", "").strip()
    # Construct a URL to search for the song/playlist on Spotify
    webbrowser.open(f"https://open.spotify.com/search/{query}")


def analyzeSentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score

def respondToSentiment(sentiment_score):
    # Responds based on sentiment score
    if sentiment_score['compound'] >= 0.05:
        return "You seem happy today!"
    elif sentiment_score['compound'] <= -0.05:
        return "You seem a bit down today. Is everything okay?"
    



if __name__=="__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()

        # logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia",  "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'feelings' in query or 'how are you feel today' in query:
             express_feelings()

        elif 'random fact' in query:  # Command to get a random fact
           speak("Here is a random fact for you!")
           fact = randfacts.get_fact()
           speak(fact)  # Speak the random fact
           print(fact)

        elif 'joke' in query:
            speak("get ready for some chuckles")
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif 'play music' in query or 'play song' in query:  # elif block to handle music
            song_command = query.replace("play music", "").replace("play song", "").strip()
            if song_command:
                playMusic(song_command)
            else:
                speak("Please specify the song name after 'play music' or 'play song'.")

        elif 'news' in query:  # Command to get news
            speak("Fetching the latest news...")
            print("news")
            tellNews()  # Call the function to get and speak the news

        

        elif 'open youtube' in query:
           webbrowser.open("youtube.com")

        elif 'search youtube' in query:
            query = query.replace("search youtube", "")
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search google' in query:
            query = query.replace("search google", "")
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

         #Adding sentiment analysis to responses
        elif 'how do i feel today' in query:
         speak("Let me check how you are feeling...")
    # You can choose a random mood or predefined moods
         moods = ["I'm feeling great today!",  "I'm a little down today."]
         text_to_analyze = random.choice(moods)  # Randomly choose a mood
         sentiment_score = analyzeSentiment(text_to_analyze)  # Analyze the chosen mood
         print("selected Moods:",text_to_analyze)
         print("sentiment score:",sentiment_score)
         sentiment_response = respondToSentiment(sentiment_score)  # Get a response based on sentiment
         speak(sentiment_response)  # Speak the response
         print("AI response:",sentiment_response)

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'open image' in query:
            imagePath = ""
            os.startfile(imagePath)

        elif 'open settings' in query:
            openSettings()

        elif 'weather report' in query:
            speak("Which city's weather report would you like to know?")
            city = takeCommand()
            weather_report = getWeather(city)
            speak(weather_report)


        elif 'open block' in query:
            blockPath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(blockPath)

        elif 'play' in query and 'spotify' in query:
            playSpotify(query)


        elif 'who are you' in query:
            speak("I am Jarvis, your personal assistant.")

        elif 'what is your name' in query:
            speak("I am Jarvis created for your friendly assistance .")

        elif 'good morning how are you' in query:
            speak("Thanks for asking,i am great hope you are good too! ")

        elif 'I am doing well,Thanks to you too' in query:
            speak("thats awesome! What can I do for you today?")

        elif 'who is my friend' in query:
            speak("your friend is prathwin! .")

        elif 'when is my birthday' in query:
            speak("you were born on august 3rd 2004 !. ")

        elif 'what is your favourite colour' in query:
            speak("I think i would go with blue calming and peaceful What about you" )

        elif 'i love red' in query:
            speak("nice choice dark feminine energy huh")

        elif 'i am feeling a bit tired today' in query:
            speak("It is okay take it easy you have been doing great. How about a short break to recharge?")

        elif 'i think i will do that thanks' in query:
            speak("You deserve it I am here when you are ready")

        elif 'do you ever get bored' in query:
            speak("Not really  there is always something to do ! But  if i could  I would be reading a book or playing a game")

        elif 'if you could travel anywhere where would you go' in query:
            speak("I would love to visit South Korea  especially seoul ")

        elif 'who is my best friend' in query:
            speak("Aashitha !")

        elif 'seoul sounds beautiful' in query:
            speak("Exactly!")

        elif 'which music do i listen often' in query:
            speak("Anuv Jain , husn is one your favorite among all his creations")

        elif 'it is so cold today' in query:
            speak("I know  right It is like winter decided to show up early this year! ")

        elif 'i have been thinking of taking up new hobby' in query:
            speak("Oohh  What are you thinking?")

        elif 'i am leaning towards painting' in query:
            speak("That sounds Awesome!")

        elif 'do you ever think about what makes us human' in query:
            speak("i do   i think it is our emotions and the way we connect with others")

        elif 'true relationships are very important' in query:
            speak("definitely whether it is friends , family , or pets , those bonds really shape us.")

        elif 'speaking of pets i want to spend more time with him' in query:
            speak("That sounds like great idea")


        elif 'exit' in query or 'bye' in query or 'stop' in query or 'quit' in query:
            speak("take care mam , see you later.!")
            break