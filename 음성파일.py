from gtts import gTTS
import playsound
import os

text = "안녕하세요, 저는 정은지 입니다. 잘 부탁드립니다."

tts = gTTS(text=text, lang='ko')

tts.save("hello.mp3")

os.system("start hello.mp3")
