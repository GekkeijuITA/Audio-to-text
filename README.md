# Audio-to-Text :it:

Questo progetto ti permette di trascrivere file audio in formato .mp3 (o altri formati) su un file di testo. Il progetto utilizza il sistema di riconoscimento vocale di Google, ma tieni presente che potrebbe non essere sempre affidabile.
## Descrizione

Il progetto utilizza la libreria SpeechRecognition di Python per accedere al servizio di riconoscimento vocale di Google e trasformare l'audio in testo. Il file audio deve essere convertito in formato WAV utilizzando la libreria FFmpeg prima di poter essere trascritto. Attualmente, il progetto trascrive solo un file audio alla volta e richiede che il file audio sia rinominato in "audio.mp3".
## Utilizzo

Per utilizzare il progetto, segui questi passaggi:

1. Assicurati di avere Python e le librerie SpeechRecognition e FFmpeg installate sul tuo computer.
2. Scarica il file audio che vuoi trascrivere e rinominalo in "audio.mp3".
3. Esegui il file Python "audio_to_text.py" per convertire il file audio in formato WAV e trascriverlo in un file di testo chiamato "transcription.txt".

## Ringraziamenti

Questo progetto utilizza le librerie SpeechRecognition e FFmpeg, che sono state sviluppate da terze parti. Ringraziamo gli autori di queste librerie per il loro lavoro.

Speriamo che questo progetto ti sia utile per trascrivere i tuoi file audio in formato di testo. Tieni presente che il servizio di riconoscimento vocale di Google potrebbe non essere sempre affidabile, quindi ti consigliamo di verificare sempre la trascrizione risultante.

***

# Audio-to-Text :en:

This is a project for transcribing audio files in .mp3 (or other formats) to a text file. The project uses Google's speech recognition system, but please note that it may not always be reliable.

## Description

The project uses the SpeechRecognition library in Python to access Google's speech recognition service and convert audio to text. The audio file must be converted to WAV format using the FFmpeg library before it can be transcribed. Currently, the project transcribes only one audio file at a time and requires that the audio file be renamed to "audio.mp3".

## Usage

To use the project, follow these steps:

1. Make sure you have Python and the SpeechRecognition and FFmpeg libraries installed on your computer.
2. Download the audio file you want to transcribe and rename it to "audio.mp3".
3. Run the "audio_to_text.py" Python file to convert the audio file to WAV format and transcribe it to a text file named "transcription.txt".

## Acknowledgments

This project uses the SpeechRecognition and FFmpeg libraries, which were developed by third parties. We thank the authors of these libraries for their work.

We hope this project is useful for transcribing your audio files to text. Please note that Google's speech recognition service may not always be reliable, so we recommend verifying the resulting transcription.