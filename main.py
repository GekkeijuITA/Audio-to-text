import speech_recognition as sr
import subprocess
import os
import logging

logging.basicConfig(level=logging.WARNING)
audio_format = ['.mp3', '.wav', '.m4a']


def get_file_name(audio_file):
    file_name = audio_file.split('.')[0]
    return file_name


def convert_to_wav(audio_file, title):
    if os.path.exists(title + 'wav'):
        os.remove(title + 'wav')
    subprocess.call(['ffmpeg', '-i', audio_file, '-vn', '-acodec',
                    'pcm_s16le', '-ar', '44100', '-ac', '2', title + 'wav'])


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


def audio_to_text(audio_file):
    title = get_file_name(audio_file)
    convert_to_wav(audio_file, title)
    with open(title + ".txt", 'w', encoding='utf-8') as file:
        file.write(transcribe_audio(audio_file, language))


language = 'it-IT'
# count files in directory
count = len([name for name in os.listdir('.') if os.path.isfile(
    name) and name.endswith(tuple(audio_format))])
if count > 0:
    print('Transcribing audio files...')
    for audio_file in os.listdir("."):
        if audio_file.endswith(tuple(audio_format)):
            audio_to_text(audio_file)
else:
    print('No audio files found in the directory')
