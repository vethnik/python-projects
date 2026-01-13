import pyttsx3 
# pyttsx3 is a library used to convert 'text to speech'
engine=pyttsx3.init()
# 'engine=pyttsx3.init()'  this is used to create a speech engine
print("Hello i am a Speaker")

while True:

    x=input("What should i pronounce: ")
    if x=='exit':
        print("Exiting......")
        engine.say("Exiting")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()