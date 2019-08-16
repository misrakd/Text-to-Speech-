from gtts import gTTS
import os

text = open(input("Enter file name: "),"rt")
# make sure that file is already existed  
tts = gTTS(text.read(), lang='en', slow=False)
tts.save("tts.mp3")
os.system("tts.mp3")
