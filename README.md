# Audio-to-Text :it:

Questo progetto ti permette di trascrivere file audio in formato .mp3 (o altri formati) su un file di testo. Il progetto utilizza il sistema di riconoscimento vocale di Google, ma tieni presente che potrebbe non essere sempre affidabile.
## Descrizione

Il progetto utilizza la libreria SpeechRecognition di Python per accedere al servizio di riconoscimento vocale di Google e trasformare l'audio in testo. Il file audio deve essere convertito in formato WAV utilizzando la libreria FFmpeg prima di poter essere trascritto. Attualmente, il progetto trascrive solo un file audio alla volta.
## Utilizzo

Per utilizzare il progetto, segui questi passaggi:

1. Scarica il progetto dal repository GitHub.
2. Assicurati di avere Python e le librerie SpeechRecognition e FFmpeg installate sul tuo computer.
3. Apri il terminale o il prompt dei comandi e vai nella directory del progetto.
4. Esegui il comando `pip install -r requirements.txt` per installare le dipendenze del progetto.
5. Scarica il file audio che vuoi trascrivere nella directory del progetto.
6. Esegui il comando `python audio_to_text.py <nome_file_audio>` dove `<nome_file_audio>` è il nome del file audio che vuoi trascrivere.
7. Il file trascritto verrà salvato nella stessa directory del file audio con lo stesso nome del file audio e l'estensione ".txt".

Il file di testo generato si troverà nella stessa directory del file audio.

## Ringraziamenti

Questo progetto utilizza le librerie SpeechRecognition e FFmpeg, che sono state sviluppate da terze parti. Ringraziamo gli autori di queste librerie per il loro lavoro.

Speriamo che questo progetto ti sia utile per trascrivere i tuoi file audio in formato di testo.
:warning: **Tieni presente che il servizio di riconoscimento vocale di Google potrebbe non essere sempre affidabile, quindi ti consigliamo di verificare sempre la trascrizione risultante.** :warning:

## Futuro del progetto

Al momento, il progetto è in fase di sviluppo e potrebbero essere apportate alcune modifiche e aggiornamenti in futuro. Alcune possibili migliorie includono:

- Aggiunta di supporto per altri formati audio oltre a .mp3. :white_check_mark:
- Possibilità di trascrivere più file audio contemporaneamente. :white_check_mark:
- Miglioramento della precisione della trascrizione attraverso l'utilizzo di tecniche di elaborazione del linguaggio naturale. :x:
- Implementazione di un'interfaccia utente grafica per semplificare l'uso del programma. :x:

Se hai suggerimenti o idee per migliorare il progetto, non esitare a contattarci o a contribuire al progetto attraverso GitHub. 

***

# Audio-to-Text :uk:

This is a project for transcribing audio files in .mp3 (or other formats) to a text file. The project uses Google's speech recognition system, but please note that it may not always be reliable.

## Description

The project uses the SpeechRecognition library in Python to access Google's speech recognition service and convert audio to text. The audio file must be converted to WAV format using the FFmpeg library before it can be transcribed. Currently, the project transcribes only one audio file at a time.

## Usage

To use the project, follow these steps:

1. Download the project from the GitHub repository.
2. Make sure you have Python and the SpeechRecognition and FFmpeg libraries installed on your computer.
3. Open the terminal or command prompt and navigate to the project directory.
4. Run the command `pip install -r requirements.txt` to install the project dependencies.
5. Download the audio file you want to transcribe to the project directory.
6. Run the command `python audio_to_text.py <audio_file_name>` where `<audio_file_name>` is the name of the audio file you want to transcribe.
7. The transcribed file will be saved to the same directory as the audio file with the same name as the audio file and the extension ".txt".

The generated text file will be located in the same directory as the audio file.

## Acknowledgments

This project uses the SpeechRecognition and FFmpeg libraries, which were developed by third parties. We thank the authors of these libraries for their work.

We hope this project is useful for transcribing your audio files to text. 
:warning: **Please note that Google's speech recognition service may not always be reliable, so we recommend verifying the resulting transcription.** :warning:
## Future of the Project

Currently, the project is under development and there may be some modifications and updates in the future. Some possible improvements include:

- Adding support for other audio formats besides .mp3. :white_check_mark:
- Allowing for transcription of multiple audio files simultaneously. :white_check_mark:
- Improving transcription accuracy through the use of natural language processing techniques. :x:
- Implementing a graphical user interface to simplify program usage. :x:

If you have any suggestions or ideas for improving the project, feel free to contact us or contribute to the project through GitHub.