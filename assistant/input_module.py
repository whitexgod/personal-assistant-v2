import speech_recognition as sr

#process1
def take_command():
    i=input("Me :")
    return i

#process2
def take_input():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")

    except Exception as e:
        #print(e)

        #print("Say that again please!")
        return "None"

    return query.lower()

