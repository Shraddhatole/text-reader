import os
from gtts import gTTS

# from playsound import playsound


# English
with open("D:/images3/textFiles/Rus.txt",encoding="utf-8") as file:
 t = gTTS(file.read(), lang="ru",tld="co.in")
t.save("russian.mp3")
os.startfile("russian.mp3")