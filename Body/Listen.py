import speech_recognition as sr
from googletrans import Translator

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-hi")

    except:
        return ""
    
    query = str(query).lower()
    return query

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"AI : {data}.")
    return data

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data
