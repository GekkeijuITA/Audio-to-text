import speech_recognition as sr
import subprocess
import os

def convert_to_wav(audio_file):
    if os.path.exists('audio.wav'):
        os.remove('audio.wav')
    subprocess.call(['ffmpeg', '-i', audio_file, '-vn', '-acodec',
                    'pcm_s16le', '-ar', '44100', '-ac', '2', 'audio.wav'])


def transcribe_audio(audio_file, language):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        print('Sorry, I could not understand audio')
    except sr.RequestError as e:
        print('Sorry, my speech service is down {0}'.format(e))


language = 'it-IT'

convert_to_wav('audio.mp3')

audio_file = 'audio.wav'

with open('trascrizione.txt' , 'w' , encoding='utf-8') as file:
    file.write(transcribe_audio(audio_file, language))