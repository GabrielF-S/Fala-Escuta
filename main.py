from os import close
import speech_recognition as sr
import gtts
from playsound import playsound
import time
import multiprocessing

def frase():
    frase = "Pode falar agora"

    fala = gtts.gTTS(frase, lang="pt-BR")
    fala.save("Inicio.mp3")

    frase2= "O que você disse foi: "
    fala2 = gtts.gTTS(frase2, lang="pt-BR")
    fala2.save("Meio.mp3")

    frase3 = "Isso é tudo pessoal!"
    fala3 = gtts.gTTS(frase3,lang="pt-BR")
    fala3.save("Fim.mp3")

def captarAudio():
    rec =sr.Recognizer()
    # print(sr.Microphone().list_microphone_names())
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        play = multiprocessing.Process(target=playsound, args=("Inicio.mp3",))
        play.start()
        audio = rec.listen(mic)
        tempo1 =time.time()
        texto = rec.recognize_google(audio, language ="pt-Br")
        tempo2 = time.time()
        tempoFinal = tempo2-tempo1
    dito = gtts.gTTS(texto, lang="pt-BR")

    dito.save("voice.mp3")

    fala(tempoFinal)
        

def fala(pausa):
    try:
        play = multiprocessing.Process(target=playsound, args=("Meio.mp3",))
        play.start()
        time.sleep(3)
        play = multiprocessing.Process(target=playsound, args=("voice.mp3",))
        play.start()
        time.sleep(pausa)
        play = multiprocessing.Process(target=playsound, args=("Fim.mp3",))
        play.start()
    except:
        playsound("voice.mp3")
   


def main():
    frase()
    captarAudio()
    

if __name__ == "__main__":
    main()