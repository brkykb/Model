from gtts import gTTS
import pygame
import os


def respond(text):
    print(f"Alya: {text}")
    tts = gTTS(text=text, lang='tr')
    tts.save("response.mp3")

    # pygame ile ses oynatma
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

    os.remove("response.mp3")
