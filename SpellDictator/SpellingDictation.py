#!/bin/python3
import pandas as pd
from csv import reader
import pyttsx3
import csv

from csv import DictReader

import gtts
from playsound import playsound


import pyttsx3

engine = pyttsx3.init()

def readfiles(Currentfile,Wrongspell,Correctspell):
    with open(Currentfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:

            #spellword = engine


            engine.say(str(row))
            print(row)
            engine.runAndWait()
            my_input = input("Send the desired iput| 1 for False | 0 for True")
            print(my_input)

            if int(my_input) == 1:
                with open(Wrongspell, 'a',newline='') as csvfile:
                    print("inside wrong spelling ="+str(row))
                    # creating a csv dict writer object
                    writer = csv.writer(csvfile)

                    # writing headers (field names)
                    writer.writerow(row)

                    # writing data rows


            else:
                with open(Correctspell, 'a', newline='') as csvfile:
                    # creating a csv dict writer object
                    writer = csv.writer(csvfile)

                    # writing headers (field names)
                    writer.writerow(row)

                    # writing data rows



readfiles("/Users/manishreddybendhi/PycharmProjects/SpellingsVirtualEnv/SpellingSheets/MainSpellings.csv"
          ,"/Users/manishreddybendhi/PycharmProjects/SpellingsVirtualEnv/SpellingSheets/WrongSpelling.csv",
          "/Users/manishreddybendhi/PycharmProjects/SpellingsVirtualEnv/SpellingSheets/CorrectSpelling.csv")




