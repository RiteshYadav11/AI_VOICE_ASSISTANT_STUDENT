from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.Speak import Speak
import pathlib
from Body.Listen import MicExecution

scriptDirectory = pathlib.Path().absolute() #This line of code is getting the absolute path of the current directory where the Python script is located using the pathlib library. The absolute() method returns the absolute path of the directory.

options = Options() # This allows you to set various options and preferences for the webdriver.
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver,options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
Speak("Initializing The Whatsapp Software.")

ListWeb = {'Aman' : "+917385378799",
            'Anurodh': "+91 77158 00875",
            "Rahul": '+919372524724',
            "Amit(ltce)":"+918108914974"}

def WhatsappSender(Name):
    Name = Name.capitalize()
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(10)
    try:
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        Speak("Message Sent")
        
    except:
        print("Invalid Number")

