#!/usr/bin/python3
#
#Purpose: Translate morse code to english and english to morse code. Simulate morse code transmitter.
#Morse code basics:
# dot duration is basic unit of of time measurement
# dash = 3 dots
# each dot or dash within a character is followed by a period of signal absence, SPACE, equal to dot duration
# letters seperated by space duration= 3 dots
# words seperates by space duration= 7 dots
# speed for PARIS(typical language 5 character long) = 20 words/min = 60 ms dot
# speed CODEX(5 character radom) = 20 words/min = 50 ms 
# Radiotelegraph license= 20 words per min PARIS
# using 700hz

import numpy as np
from scipy.io.wavfile import write
from pygame import mixer
import time

###################### Audio Settings ######################

#initialize the audio mixer that will let me play the audio
mixer.init()
#Had to create my own tone wav files using a seperate
#audio generator program I made
DOT= mixer.music.load("morse_dot1.wav")
DASH= mixer.music.load("morse_dash.wav")

#this function generate a specific tone based on single dot or dash values as input
def sound(wave):
	if wave=="dot":
		DOT	
		mixer.music.play()
#had to put this sleep function to let the tone finish playing or else python will continue to the next command way before it is done.
		time.sleep(.1)
	else:
		DASH
		mixer.music.play()
		time.sleep(.3)
	return

#this function is to start translating the user input into morse code audio
#adjusted sleep time to go hand in hand with morse code basic time delays
#" " standing for character seperation and "/" for word seperation
def play_morse(code):
	for i in range(len(code)):
		if code[i]==".":
			sound("dot")
			time.sleep(.1)
		elif code[i]=="-":
			sound("dash")
			time.sleep(.1)
		elif code[i]==" ":
			time.sleep(.3)
			time.sleep(.1)
		elif code[i]=="/":
			time.sleep(.7)
			time.sleep(.1)
	time.sleep(.1)
	return

############## Character Translation Settings ##############

#translation dictionary keys for english to morse code:
e2m_dic={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","&":".-...","'":".----.","@":".--.-.",")":"-.--.-","(":"-.--.",":":"---...",",":"--..--","=":"-...-","!":"-.-.--",".":".-.-.-","-":"-....-","+":".-.-.","\"":".-..-.","?":"..--..","/":"-..-."," ":"/"}

#translation dictionary keys for morse code to english:
m2e_dic= {y:x for x,y in e2m_dic.items()}

#Function for english to morse translation:
def eng2morse(string):
	characters= string.upper()
	characters_list=[]
	for i in range(len(characters)):
		characters_list.append(characters[i])
		characters_list[i]= e2m_dic[characters_list[i]]
	translation=' '.join(characters_list)
	return translation

#Function for morse code to english translation:
def morse2eng(string):
	translation=[]
	word_list= string.split("/")
	for i in range(len(word_list)):
		word= word_list[i]
		word_letters= word.split(" ")
		for k in range(len(word_letters)):
			word_letters[k]= m2e_dic[word_letters[k]]
		word=''.join(word_letters)
		translation.append(word)
	translation=' '.join(translation)
	return translation

################ User Interaction Functions ################

#Function to execute user desired mode, translator or real time transmitter.
def execute(mode):
	if mode== "t":
#If wanting to translate, it will ask what type of translation and if audio is desired.
#The audio is made optional as not everyone will want to hear it, some might just want a quick text translation.
		language= input("\nTranslate English text to Morse Code [e2m] or Morse Code to English text [m2e]? Choose e2m or m2e:\n")
		translation= translate(language)
		if language=="e2m":
			hear_code= input("\nDo you want Morse Code audio output as well? yes or no:\n")
			print("\nYour translation is ready:")
			print(translation)
			if hear_code=="yes":
				play_morse(translation)
#Since transmitter part was not finished(it was more of an extra thing if there was more time), I decided to leave this message for users to see.
#I decided to keep this because I imagined myself building this project for an internet type of application. I easily pick up from here after the class is over, and seems more realistic.
		else:
			print("\nYour translation is ready:")
			print(translation)
			return
	elif mode== "s":
		print("\nSorry this module is underconstruction, please try again soon.\n\nThank You!\n")
		exit(0)


#Function to go into translation mode based on user language input.
def translate(language):
	if language=="e2m":
		user_text= input("\nType your English message:\n")
		translation= eng2morse(user_text)
		return translation
	if language=="m2e":
#Because of the way my dictionary is set up (its format), I must let users know how to properly write the morse code for successful translation
		user_text= input("\nType your Morse Code message: (letters seperated by spaces and words seperated by forward slashes)\n")
		translation= morse2eng(user_text)
		return translation

######################## Program Execution #################

#Ask user what mode they want:
mode= input("\nDo you want to translate morse code [t], or simulate a morse code transmitter [s]? Type t or s:\n")
#Use a cascade of predifined functions to excute the user's wishes:
execute(mode)
