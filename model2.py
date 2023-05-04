import os
from gtts import gTTS
from flask import Flask, render_template, request


def robot():
 return render_template('robot.html')


# English
with open("D:/images2/textFiles/Eng.txt", encoding="utf-8") as file:
    t = gTTS(file.read(), lang="en", tld="co.in")
    robot();
    t.save("english.mp3")
    os.startfile("english.mp3")



