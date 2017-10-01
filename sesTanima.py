import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as kaynak:
        ses = r.listen(kaynak,timeout = None)
        try:
            print(r.recognize_google(ses,language="tr-TR"))
        except sr.UnknownValueError:
            print("Anlamadım.")
        except sr.RequestError:
            print("Bad Request")
