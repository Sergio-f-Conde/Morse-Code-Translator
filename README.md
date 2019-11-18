# Morse-Code-Translator

This application has both visual and auditory capabilities. The main code is located in Morse.py, with supporting audio files for the dot and dash sounds. Mourse_sound.py contains the code I used to create these audio files.

The program first asks users what mode they want to use, translator or transmitter. The transmitter mode was a fun idea I had to add to the project, still working on it so it is not part of the main project yet. I kept the option to add a more realistic web application type of feel to the project. 

Since the translator mode is the only available one, it will then ask users what they want to translate: English to Morse code or Morse code to English.

If English to Morse code is selected, it will further ask if users want to hear the Morse code audio of the translation. Choosing no will display the Morse code translation on the screen only, while choosing yes will display the code and play the audio on the default audio device of the system. 

If Morse code to English is selected, it will let users know how to properly type in the Morse code so that the computer successfully translates it (I have a specific dictionary format that users must follow).
