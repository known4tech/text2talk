import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Yatin Kumar")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak (or 'x' to exit): ")
        if x =="x":
            engine.say("Bye bye friend, see you soon!")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()