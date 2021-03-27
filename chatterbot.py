#CLEANING:
#stopword=is ,are, that, the, and, or ,how ,etc
#remove number
#remove punctuation
#all letters to lower case

#STEP1:
#.lower()-- convert into lowercase 
#.strip()-- remove white space before and after letters
#\d+ --remove integer number
#string library--to get all punctuation for removing
#nltk library:-stopwords['english']=an ,the ,that, how ,is ,etc
#.strip():- so while choosing words the 'before and after space' doesnt count




#import tensorflow as tf
#tf.__version__
#pip install sqlalchemy --upgrade

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
#if any error for 'en' use:=  python -m spacy download en
bot=ChatBot('Bot')
trainer=ChatterBotCorpusTrainer(bot)

corpus_path=r'C:\Users\omkar desai\Desktop\Artificial Inteligence\chatterbot-corpus-master\chatterbot_corpus\data\english\\'
#as path=r'c\user\\ai'+'computer.yml'----ok
#r'c\user\\ai\'+'computer.yml'---not ok error
#r'c\user\\ai\\'+'computer.yml'---ok no error,efficient


for file in os.listdir(corpus_path):
    
    trainer.train(corpus_path + file)
    
while True:
    message = input('You:')
    print(message)
    if message.strip()=="Bye":
        print("ChatBot : Bye")
        break
    else:
        reply = bot.get_response(message)
        print("ChatBot:",reply)

#pip install SpeechRecognition
import speech_recognition as sr
#pip install pyttsx3
import pyttsx3

#pip install pyaudio





























