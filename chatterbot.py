from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

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






























