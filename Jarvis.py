from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Body.Listen import Listen
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution
from Features.game import game_play
from Features.ScheduleMyDay import schedule
from Features.ShowMySchedule import showschedule
import pyautogui
import os
from pygame import mixer
from plyer import notification
from Features.keyboard import volumedown
from Features.keyboard import volumeup
from Features.SpeedTest import check_internet_speed
from time import sleep
from Features.Screenshot import screenshot

def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Your Assistant, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "game" in Data:
            game_play()

        elif "screenshot" in Data:
            screenshot(Data)

        elif "news" in Data:
            from Features.News import latestnews
            latestnews()

        elif "show my schedule" in Data:
            showschedule(Data)

        elif "schedule" in Data:
            schedule(Data)

        elif "click my photo" in Data:
            import pyautogui
            import time
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            time.sleep(5)
            pyautogui.press("enter")

        elif "internet speed" in Data:
            check_internet_speed()

        elif "volume up" in Data:
            from Features.keyboard import volumeup
            Speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in Data:
            from Features.keyboard import volumedown
            Speak("Turning volume down, sir")
            volumedown()

        
        elif "focus mode" in Data:
            from Features.FocusMode import is_admin
            Speak("Are you sure that you want to enter focus mode Please Speak Yes Or No")
            a = Listen().lower()
            if (a=="yes"):
                Speak("Entering the focus mode....")
                is_admin()
                pass
            
            else:
                pass
        
        elif "show my focus" in Data:
            from Features.FocusGraph import focus_graph
            focus_graph()

        elif "ipl score" in Data:
            from Features.Score import get_score
            get_score()

        elif"add assignment" in Data:
            from Features.Assignment import add_assignment
            add_assignment()

        elif"show assignment" in Data:
            from Features.Assignment import show_assignments
            show_assignments()

        elif"check assignment" in Data:
            from Features.Assignment import check_assignment
            check_assignment()

        elif"delete assignment" in Data:
            from Features.Assignment import delete_assignment
            delete_assignment()


        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)

        elif"go to sleep" in Data:
            exit()

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def WakeupDetected():

    while True:

        queery = Listen().lower()

        if "wake up" in queery:
            print("")
            MainExecution()
        
        else:
            pass
WakeupDetected()
