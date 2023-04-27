#import speech_recognition as sr
import subprocess
import os
import magic

mime = magic.Magic(mime=True)
audio_format = ['.mp3', '.wav', '.m4a']

def get_file_name(audio_file):
    file_name = audio_file.split('.')[0]
    return file_name

def convert_to_wav(audio_file , title):
    if os.path.exists(title + 'wav'):
        os.remove(title + 'wav')
    subprocess.call(['ffmpeg', '-i', audio_file, '-vn', '-acodec',
                    'pcm_s16le', '-ar', '44100', '-ac', '2', title + 'wav'])

def transcribe_audio(audio_file, language):
    return get_file_name(audio_file)
    #r = sr.Recognizer()
    #with sr.AudioFile(audio_file) as source:
    #    audio = r.record(source)
    #try:
    #    text = r.recognize_google(audio, language=language)
    #    return text
    #except sr.UnknownValueError:
    #    print('Sorry, I could not understand the audio ' + audio_file)
    #except sr.RequestError as e:
    #    print('Sorry, my speech service is down {0}'.format(e))

def audio_to_text(audiofile):
    title = get_file_name(audiofile)
    convert_to_wav(audio_file , title)
    with open(title + ".txt" , 'w' , encoding='utf-8') as file:
        file.write(transcribe_audio(audio_file, language))

language = 'it-IT'

for audio_file in os.listdir("."):
    file_type = mime.from_file(audio_file)
    if file_type.startswith("audio/"):
        audio_to_text(audio_file)