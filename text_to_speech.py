import pyttsx3

def text_to_speech(text):
   
    engine = pyttsx3.init()

   
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', rate - 50)  

 
    volume = engine.getProperty('volume')  
    engine.setProperty('volume', volume + 0.25)  

 
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
   
    user_input = input("Digite o texto que você deseja que seja lido em voz alta: ")
    text_to_speech(user_input)
