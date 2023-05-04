import os
from gtts import gTTS


# English
with open("D:/images5/textFiles/saved_img.txt",encoding="utf-8") as file:
 t = gTTS(file.read(), lang="en",tld="co.in")
t.save("video_text.mp3")
os.startfile("video_text.mp3")

