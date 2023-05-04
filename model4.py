import os
from gtts import gTTS

# from playsound import playsound


# English
with open("D:/images4/textFiles/jap.txt",encoding="utf-8") as file:
 t = gTTS(file.read(), lang="ja",tld="co.in")
t.save("japanese.mp3")
os.startfile("japanese.mp3")