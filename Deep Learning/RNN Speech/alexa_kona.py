import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    try:
        with sr.Microphone() as mic:
            print('listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'kona' in cmd:
                cmd = cmd.replace('kona', '')
                print(cmd)
                return cmd
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None

def run():
    while True:
        cmd = hear()
        if cmd:
            print(cmd)
            if 'play' in cmd:
                song = cmd.replace('play', '').strip()
                speak('playing ' + song)
                pk.playonyt(song)
            elif 'stop' in cmd:
                speak('stopping')
                break
        else:
            speak("I didn't catch that")

if __name__ == "__main__":
    run()
