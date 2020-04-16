import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am kiya. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    doct={'doctor sneha':1, 'doctor karan':2, 'doctor rishi':3, 'doctor ishika':4, 'doctor soni':5, 'doctor riya':6, 'doctor sumi':7,\
         'doctor simran':8, 'doctor suzi':9,'doctor ravi':10, 'doctor Rani':11,'doctor Rahul':12,'doctor khusi':13, 'doctor niraj':14,'docor pankaj':15,\
             'doctor subham':16,'doctor suman':17,'doctor jyoti':18,'doctor sunil':19,'doctor trisha':20,'dr sneha':1, 'dr karan':2,\
                  'dr rishi':3, 'dr ishika':4, 'dr soni':5, 'dr riya':6, 'dr sumi':7, 'dr simran':8, 'dr suzi':9,'dr ravi':10,\
                       'dr Rani':11,'dr Rahul':12,'dr khusi':13, 'dr niraj':14,'dr pankaj':15,'dr subham':16,'dr suman':17,\
                           'dr jyoti':18,'dr sunil':19,'dr trisha':20}
    eye_specialist=["doctor soni","doctor riya"]
    child_specialist=['doctor karan','doctor rishi']
    Surgeon_specialist=['doctor sneha','doctor ishika']
    Neurologist=['doctor sumi']
    Emergency_Physician=['doctor simran','doctor ravi']
    urologist=['doctor trisha','doctor jyoti']
    Radiologist=['doctor subham','doctor suzi']
    medical_shop=['Ground_floor','seven floor']
    Registration_of_patient=['Ground_floor']
    blood_bank=['seven floor']
    ambulance_number=['123455678']


    floor={'General ward': 'first floor','CCU Ward':'second floor','ICU ward':'Third floor'}

    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'cabin number' in query:
            speak("Yes i may help you with this.  which doctor cabin number you want.")
            comd = takeCommand().lower()
            if 'dr' in comd:
                comd.replace('dr','doctor')
            speak(f' doctor cabin  number is {doct[comd]}')

        elif 'specialist doctor' in query:
            speak("Yes i help you with this. which specialist doctor you want.") 
            comd=takeCommand().lower()
            print(comd)
            if 'eye specialist' or 'I specialist' in comd:
                speak(f' eye specialist is {eye_specialist}')
            elif 'child specialist' in comd:    
                speak(f' child specialist is {child_specialist}')
            elif 'Surgeon specialist' in comd:
                speak(f' Surgeon specialist is {Surgeon_specialist}')
            elif 'Neurologist' in comd:   
                speak(f'Neurologist specialist is {Neurologist}')
            elif 'Emergency Physician' in comd:    
                speak(f'Emergency_Physician specialist is {Emergency_Physician}')
            elif 'urologist' in comd:
                speak(f'urologist specialist is {urologist}') 
            elif 'Radiologist' in comd:
                speak(f'Radiologist specialist is {Radiologist}') 
            else:
                speak(f'Sorry does not available doctor') 

        elif 'medical shop' in query:
            speak(f' medical shop is on seventh floor and on ground floor ')   

        
        elif 'Registration of patient' in query:
            speak(f'Registration of patient is on ground floor ')

        elif 'blood bank' in query:
            speak(f'blood bank is on 7th floor ') 

        elif 'X ray department' in query:
            speak(f'X ray department is on 8th floor ') 

        elif 'ambulance number' in query:
            speak(f'If you dial 200 our ambulance will come to your doorstep')                             


        elif 'ward number' in query:
            # speak("Yes i may help you with this. which patient ward number you want.") 
            speak(f' patient ward number is {floor} ')

        elif 'stop' or 'top' in query:
            exit()  