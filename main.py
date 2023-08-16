import speech_recognition as sr
import win32com.client
import openai
from config import apikey
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatStr = ""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User: {query}\n AI: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo:wrap inside trycatch
    speaker.Speak(response['choices'][0]['text'])
    chatStr+= f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{prompt[0:30]}.txt", "w") as f:
        f.write(text)
def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for Prompt: {prompt}\n***********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo:wrap inside trycatch
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{prompt[0:30]}.txt", "w") as f:
        f.write(text)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-us")
            print(f"User said {query}")
            return query
        except Exception as e:
            return "An Error occurred ... Please Try again "


while True:
    speaker.Speak("Hi I am your personal Artificial Intelligence helper... How can I help")
    query = take_command()
    if "Using aritificial intelligence".lower() in query.lower():
        ai(prompt=query)
    elif "Thank you".lower() in query.lower():
        exit()
    elif "reset".lower() in query.lower():
        chatStr=""
        speaker.Speak("I have reset chat")
    else:
        chat(query)
