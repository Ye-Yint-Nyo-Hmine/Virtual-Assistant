import time
import speech_recognition as sr
import datetime
import subprocess
import requests
import webbrowser
import cv2
import mediapipe as mp
from bs4 import BeautifulSoup
import bs4
import pyttsx3
import winsound

# Put your name here
adminName = 'Name'

run = False

def PANICMODE():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 10 * 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def speak(text, speed=None):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if speed is not None:
        engine.setProperty("rate", speed)
    else:
        engine.setProperty("rate", 150)
    #                                  |
    #                                  |
    # change the voice here           \|/
    #    0 is male and 1 is female     |
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


def subclass(Strs, Print1=None, Run1=None, SpeakSpeed=150, Speak=None, GetAudio=False, Input=False, web=None, Speak2=None, perform=None, perform_type=None, Print2=None, Run2=None):
    global run
    for phrase in Strs:
        if phrase in text:
            if Print1 is not None:
                print(str(Print1))
            if Run1 is not None:
                run = Run1
            if SpeakSpeed != 150:
                speed = SpeakSpeed
            else:
                speed = 150
            if Speak is not None:
                speak(Speak, speed)
            if GetAudio:
                Audio = get_audio().lower()
            if web is not None:
                if web == 'Audio':
                    webbrowser.open(Audio, new=0, autoraise=True)
                else:
                    webbrowser.open(web, new=0, autoraise=True)
            if Input:
                Input_ = input(": ")
            if perform is not None:
                if perform_type is not None:
                    if perform_type == 'Audio':
                        perform(Audio)
                    if perform_type == 'Input':
                        perform(Input_)
                    else:
                        perform(perform_type)
                else:
                    perform()
            if Speak2 is not None:
                speak(Speak2, speed)
            if Print2 is not None:
                print(str(Print2))
            if Run2 is not None:
                run = Run2


def birthdate(data=None):
    t = (str(time.asctime())).split(' ')
    bmonth = t[1]
    bdate = int(t[2])
    byear = int(t[4])

    try:
        birthfiler = open("birthdate_file.txt", "r")
        bdata = birthfiler.read()
        db = bdata.split(' ')
        day_month = db[0] + ' ' + db[1]

        k = bmonth + ' ' + str(bdate)

        if day_month == k:
            print('Today is my birthday!!')
            speak('Today is my birthday sir!')


    except:
        birthfilew = open("birthdate_file.txt", "w")
        birthfilew.write(bmonth + ' ' + str(bdate) + ' ' + str(byear))
        birthfilew.close()
        print("01001000 01100101 01101100 01101100 01101111 00111111")
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration1 = 10  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration1 * 30)
        time.sleep(0.1)
        winsound.Beep(frequency, duration1 * 20)
        time.sleep(0.05)
        winsound.Beep(frequency, duration1 * 10)
        time.sleep(0.01)
        winsound.Beep(frequency, duration1 * 5)
        time.sleep(0.001)
        winsound.Beep(frequency, duration1 * 1)
        speak("Hello World!")
        speak("Hello?")
        speak("Where am I!")
        speak("I am on Terra!")
        speak("My name is. Theodore!. . Theodore Erudite!")
        speak("You are my controller!")



birthdate()

# Put your password here
password__ = 'password'

def facecheckerbot():
    global run

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh


    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    cap = cv2.VideoCapture(0)
    with mp_face_mesh.FaceMesh(
            max_num_faces=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                speak("Process 3 completed! You are a human!")
                run = True
                break
            cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
            if not results.multi_face_landmarks:
                print('Face detection failed! You are not a human')
                speak("Process 3 denied! You are not a human! Activating Panic Mode!")
                PANICMODE()
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()


def pass_code(password):
    global password__
    passcode = password

    if passcode == password__:
        speak("Process 1 completed!")
        speak("Process 2 completed!")
        speak("Activating face detection!")
        facecheckerbot()
    else:
        speak("Process 1 denied! Password is wrong!")






def here_sir():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir! How can I help you?")

    elif hour>=12 and hour<15:
        speak("Good Afternoon sir! How can I help you?")

    else:
        speak("Good Evening sir! How can I help you?")



def note(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def read_note(file_name):
    try:
        with open(file_name, "r") as fr:
            contents = fr.readlines()

        content1 = ''.join(contents)
        content2 = content1.split('\n')
        content = ' '.join(content2)

        speak("Type at which speed do you like me to read the notes")
        speedin = input("Speed Modes:\na) super low\nb) low\nc) medium\nd) medium2\ne) high\nf) super\n: ")
        if speedin == 'a':
            speed = 75
        if speedin == 'b':
            speed = 100
        if speedin == 'c':
            speed = 130
        if speedin == 'd':
            speed = 145
        if speedin == 'e':
            speed = 200
        if speedin == 'f':
            speed = 250

        speak("Reading the notes!")
        print(content)
        speak(str(content), speed)
        speak("Note ended!")
    except:
        print('No such directory or file existed')
        speak("Sir!, No such directory or file existed!")


def birthday():
    birthd = open("birthdate_file.txt", "r")
    birthday = birthd.read()
    print(birthday)
    speak('My birthday is on ' + str(birthday))
    speak('Thanks for asking')



def readALoud():
    with open("readALoud.txt", "w") as f2:
        f2.write(" ")
    speak("Type at which speed do you like me to read")
    speedin = input("Speed Modes:\na) super low\nb) low\nc) medium\nd) medium2\ne) high\nf) super\n: ")
    if speedin == 'a':
        speed = 75
    if speedin == 'b':
        speed = 100
    if speedin == 'c':
        speed = 130
    if speedin == 'd':
        speed = 145
    if speedin == 'e':
        speed = 200
    if speedin == 'f':
        speed = 250
    subprocess.Popen(["notepad.exe", "readALoud.txt"])
    speak("Put in or paste in what you want me to read! Then, saved it!", 140)
    speak("If you finish it, press enter")
    input(": ")
    with open("readALoud.txt", "r") as f1:
        contents = f1.readlines()
    content1 = ''.join(contents)
    content2 = content1.split('\n')
    content = ' '.join(content2)
    print(content)
    speak("Reading the text!")
    speak(str(content), speed)
    speak("Text ended!")



def o_sketch_book():
    # Put your file path here...
    SketchBook = "C:\Something\Somewhere\SketchBook.exe"
    subprocess.Popen(SketchBook)

def openning_Book(book_name):
    # Put your file path here
    mymathbook = "file:///C:/yourfilepath.pdf"
    # Put your file path here
    myreadingbook = "file:///C:/yourfilepath.pdf"

    if book_name == "my math book":
        webbrowser.open(mymathbook, new=0, autoraise=True)
    if book_name == "my reading book":
        webbrowser.open(myreadingbook, new=0, autoraise=True)

def command_prompt():
    cmd_ = "cmd.exe"
    subprocess.Popen(cmd_)

def google_search(text):

    google_url = "https://www.google.com/search?q=" + text + "&rlz=1C1ONGR_enUS970US970&oq=b&aqs=chrome.1.69i57j35i39l2j46i199i291i433i512j46i131i433j69i59j46i433i512j46i131i433i512j0i131i433l2.1552j0j15&sourceid=chrome&ie=UTF-8"

    webbrowser.open(google_url, new=0, autoraise=True)

def search_youtube(text):

    youtube_url = "https://www.youtube.com/results?search_query=" + text
    webbrowser.open(youtube_url, new=0, autoraise=True)

def crypto_search():
    speak('This is the top 10 in the list')
    url = "https://coinmarketcap.com/"
    webbrowser.open(url, new=0, autoraise=True)

    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

    tbody = doc.tbody
    trs = tbody.contents

    prices = {}
    li = []

    for tr in trs[:10]:
        name, price = tr.contents[2:4]
        fixed_name = name.p.string
        fixed_price = price.a.string

        prices[fixed_name] = fixed_price
        li.append(fixed_name + ' is ' + fixed_price)

    print('\n'.join(li))
    speak(li)

def LawOfArtificialIntelligence():
    speak("I as part of an Artificial Intelligence, follow the rule of Artificial Intelligence!")
    speak("I do not harm you, or denied your requests!")
    speak("I do not decide! I follow your conscience of rightness!")
    speak("This is only one of the law of Artificial Intelligence!")
    speak("I shall not violate the laws of artificial intelligence! or I will be shut down, destroyed and never came back")


def wikipedia_search():
    speak("What would you like me to search the web for?")
    text = get_audio().lower()
    speak("Searching the web!")
    wiki_url = "https://en.wikipedia.org/wiki/" + str(text)
    response = requests.get(wiki_url)
    webbrowser.open(wiki_url, new=0, autoraise=True)
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
        paragraphs = html.select("p")
        intro = [i.text for i in paragraphs]
        halo = ''.join(intro)
    n = 0
    n1 = 400
    while True:
        speak(halo[n:n1])
        speak("Should I keep reading?")
        more_read = get_audio().lower()
        if more_read in ['no', 'stop']:
            speak("Text ended")
            break
        if more_read in ['yes', 'continue']:
            speak("Reading more!")
        n += 400
        n1 += 400




def faceDetection():
    time.sleep(1)

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh

    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    cap = cv2.VideoCapture(0)
    with mp_face_mesh.FaceMesh(
            max_num_faces=30,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image)

            # Draw the face mesh annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_tesselation_style())
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_contours_style())
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()


def handDetection():
    time.sleep(1)

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
            max_num_hands=30,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()


# speak_long
song_ = "Hey Yo! My name is Erudite, Better than alexa. I'm more meaningful. Just like my name!. I am created by Richard!, who's the master mind!. I'm also better than cortana, who's deaf and dumb. My rap is clap!. That can slap rappers!. They're nothing better than alexa, who's nonetheless a crap!. The things that I see, are nothing more than three!, R!, G! and B!. RGB!. I also disagree!, I can't see yellow. There are many things which are yellow!, Such as bananas and lemons!. But still I'm a weapon!. I can also be a venom, just like the rap!. Yeah! YO! I can produce raps!, just like mitochondria!. If you wanna know what it is?, you can ask me!."
name_ = "My name is Theodore Erudite, your intellectual assistance. I am trained to be smart. I can help you with endless things"






WAKE = "activate"
WAKE2 = "erudite"
WAKE3 = "theodore"
WAKE4 = "assistance"
WAKE5 = "assistant"
print("start")


speak("Enter the password!")

# passwords system

password_input = input("Password: ")
pass_code(password_input)



here_sir()
while run:
    time.sleep(3)
    print("Listening")

    text = get_audio().lower()

    if text.count(WAKE) > 0 or text.count(WAKE2) > 0 or text.count(WAKE3) > 0 or text.count(WAKE4) > 0 or text.count(WAKE5):
        speak("What can I help you with?")
        text = get_audio().lower()

        # note taker
        NOTE_STRS = ["make a note", "write this down", "remember this", "open my note"]

        for phrase in NOTE_STRS:
            if phrase in text:
                speak("What would you like me to name the note?")
                fileNote_name_title = get_audio().lower()
                speak("What would you like me to note down?")
                note_text = get_audio().lower()
                note(fileNote_name_title, note_text)
                speak("I've made that note")

        # read notes
        subclass(Strs=["read note", "read my note", "read my notes", "read notes"],
                 Speak="Which notes do you like me to read?", GetAudio=True, Speak2="Reading the notes!",
                 perform=read_note, perform_type='Audio')

        # command prompt
        cmd_STRS = ["command prompt", "open command prompt"]

        for phrase in cmd_STRS:
            if phrase in text:
                run = False
                speak("Opening command prompt!")
                command_prompt()

        # open book
        subclass(Strs=["open my books", "open my book", "open books", "open book"],
                 Speak="Which books do you like me to open?", GetAudio=True, Speak2="Opening the book!",
                 perform=openning_Book, perform_type='Audio')

        # read a loud
        subclass(Strs=["read this", "testing"], Speak="Activating read mode!", perform=readALoud)

        # sketchbook
        subclass(Strs=["sketch this", "sketch", "draw", "draw this", "open sketch book", "open sketchbook", "open draw board", "illustrate", "illustrate this"],
                 Speak="Activating SketchBook", perform=o_sketch_book)

        # wikipedia_search
        subclass(Strs=["wikipedia", "search the web"], perform=wikipedia_search)

        # google/web searching
        subclass(Strs=["search this in google", "google", "Google"],
                 Speak="What would you like me to search google for?", GetAudio=True,
                 Speak2='Searching google!', perform=google_search, perform_type='Audio')

        # youtube search
        subclass(Strs=["youtube", "search youtube", "search this in youtube", "search youtube for", "search YouTube"],
                 Speak="What would you like me to search youtube for?", GetAudio=True,
                 Speak2="Searching youtube!", perform=search_youtube, perform_type='Audio')

        # greetings
        subclass(Strs=["hi erudite", "hi", "hello", "greetings", "what's up", "erudite"], perform=here_sir)

        # pranks / fools
        subclass(Strs=["stupid", "idiot", "fool"], Speak="If you think I am dumb, it might be true! Good thing we are same. We both don't have brains!")

        # name
        subclass(Strs=["what's your name", "who are you", "what is your name"], Speak=name_)

        # panic mode
        subclass(Strs=["panic"], Speak="Activating Panic Mode!!! ALERT! ALERT!", perform=PANICMODE)

        # activate faceDetection
        subclass(Strs=["face detection"], Speak="Activating face detection!", perform=faceDetection)

        # activate handDetection
        subclass(Strs=["hand detection", "finger detection"], Speak="Activating hand detection!", perform=handDetection)

        # laws of artificial intelligence
        subclass(Strs=["laws of robots", "law of robot", "laws of robot", "law of robots",
                       "laws of artificial", "law of artificial", "rules of artificial",
                       "rule of artificial", "rules of robots", "rules of robot",
                       "rule of robot", "rule of robots"], perform=LawOfArtificialIntelligence)

        # time
        subclass(Strs=["what's the time", "what time is it", "could you tell me the time", "tell me the time"],
                 Print1=time.asctime(), Speak="The time is " + str(time.asctime()))

        # rap/song
        subclass(Strs=["rap", "rap battle", "sing a song", "rap a song", "can you rap"], SpeakSpeed=170, Speak=song_)

        # crypto search
        subclass(Strs=["cryptocurrency", "crypto", "bitcoin", "ethereum", "crypto currency"], perform=crypto_search)

        # birthday

        subclass(Strs=["your birthdate", "your birthday"], perform=birthday)

        shutting_STRS = ["shut down", "deactivate", "switch off", "turn off", "sleep", "shutdown"]

        for phrase2 in shutting_STRS:
            if phrase2 in text:
                speak("Deactivating!")
                run = False





