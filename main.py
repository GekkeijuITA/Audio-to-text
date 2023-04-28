import speech_recognition as sr
import subprocess
import os
import logging
import PySimpleGUI as sg
import platform

logging.basicConfig(level=logging.WARNING)
audio_format = ['.mp3', '.wav', '.m4a']
folder = '.convertedFile'
language = 'it-IT'

current_platform = platform.system()

if current_platform == 'Windows':
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'windows', 'ffmpeg.exe')
elif current_platform == 'Darwin':
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'macos', 'ffmpeg')
else:
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'linux', 'ffmpeg')


def get_file_name(audio_file):
    file_name = audio_file.split('.')[0]
    return file_name

def convert_to_wav(audio_file, title):
    if os.path.exists(folder + '/' + title + '.wav'):
        os.remove(folder + '/' + title + '.wav')
    subprocess.call([ffmpeg_path, '-i', audio_file, '-vn', '-acodec',
                    'pcm_s16le', '-ar', '44100', '-ac', '2', folder + '/' + title + '.wav'])


def transcribe_audio(audio_file, language):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language=language)
        print('Transcription of ' + audio_file + ' complete')
        return text
    except sr.UnknownValueError:
        print('Sorry, I could not understand the audio ' + audio_file)
        return ''
    except sr.RequestError as e:
        print('Sorry, my speech service is down {0}'.format(e))
        return ''

def delete_files_in_folder(folder):
    for file in os.listdir(folder):
        if file.endswith(tuple(audio_format)):
            os.remove(os.path.join(folder, file))

def audio_to_text(audio_file):
    title = get_file_name(audio_file)
    convert_to_wav(audio_file, title)
    with open("transcription/" + title + ".txt", 'w', encoding='utf-8') as file:
        file.write(transcribe_audio(folder + '/' + title + '.wav', language))
    delete_files_in_folder(folder)

# Creazione della finestra
layout = [[sg.Text('Seleziona uno o più file')],
          [sg.Input(key='_FILESBROWSE_'), sg.FilesBrowse()],
          [sg.OK(), sg.Cancel()]]
window = sg.Window('Seleziona uno o più file', layout)

# Loop degli eventi
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'OK':
        files_selected = values['_FILESBROWSE_'].split(';')
        for audio_file in files_selected:
            audio_to_text(audio_file)
        break

# Chiusura della finestra
window.close()