"""
A python Desktop Artificial Inteligency, The program will be personal and this will be super cool
"""
def speak(str):
    import pyttsx3
    Artificial_voice = pyttsx3.init()
    Artificial_voice.say(str)
    Artificial_voice.runAndWait()

def introduction():
    return "Now I need to intriduce myself, I am Androme, A virtual Artificial Intelegence. And I am here to assist you in verity Task since best I can. 24 Hours a Day, 7 days a week; importing all preferences from herment places, System is now fully Operational"

def gender():
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.say("I am always tring to being constant")
    engine.setProperty('voice', voices[0].id)
    engine.say("If you want then I can change my gender, But I m just a python program by Mr.Abhinav sir")
    engine.runAndWait()

if __name__ == "__main__":
    gender()
    # import pyttsx3
    # voiceEngine = pyttsx3.init()
    # rate = voiceEngine.getProperty('rate')
    # volume = voiceEngine.getProperty('volume')
    # voice = voiceEngine.getProperty('voice')
    
    # print(rate)
    # print(volume)
    # print(voice)
    # # speak(introduction())
    # voiceEngine.setProperty('rate', 150)
    # voiceEngine.setProperty('voice', voice[1].id)
    # voiceEngine.say("Now I may it to intriduce myself, I am Friday, A virtual Artificial Intelegence. And I am here to assist you in verity Task since best I can. 24 Hours a Day, 7 days a week; importing all preferences from herment places, System is now fully Operational")
    # voiceEngine.runAndWait()
    # import pyttsx3
    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # print(voices)
    # engine.setProperty('rate', 150)
    # engine.setProperty('voice', voices[1].id)
    # engine.say("I am always tring to being constant Now I may it to intriduce myself, I am Friday, A virtual Artificial Intelegence. And I am here to assist you in verity Task since best I can. 24 Hours a Day, 7 days a week; importing all preferences from herment places, System is now fully Operational")
    # engine.setProperty('voice', voices[0].id)
    # engine.say("If you want then I can change my gender, But I m just a python program by Mr.Abhinav sir")
    # engine.runAndWait()
    