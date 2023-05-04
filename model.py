import os

from flask import render_template
from gtts import gTTS

# from playsound import playsound


# HINDI
with open("D:/images/textFiles/Hin.txt",encoding="utf-8") as file:
 t = gTTS(file.read(), lang="hi",tld="co.in")
# t.save("HINDI.mp3")
# os.startfile("HINDI.mp3")
render_template('robot.html')
t.save("HINDI.mp3")
os.startfile("HINDI.mp3")