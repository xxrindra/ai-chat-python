import os
import time
os.system('cls')
print("Questionare Chat Bot")
f = open("aichatsummary.txt", "r")
txt=f.read()
print("Oh, look at that! You've been here before! Previous Inputs:")
print(txt)
time.sleep(5)
print("(AI) What's your name traveller?")
name = str(input())
print("(AI)Why hello there, "+name+" nice to meet you!")
time.sleep(2)
print("(AI) Whats your favorite food "+name+"?")
favfood = str(input())
print("(AI) Ahhh Yes! "+favfood+" Thats my favorite too!")
time.sleep(3)
print("(AI) Hmmm... aha! What about your favorite drink, "+name+"!")
favdrink = str(input())
#if favdrink.find("Coke") > -1:
 #print("(AI) Coke is bland!")
#if favdrink.find("Sprite") > -1:
# print("(AI) Sprite is awesome!!")
print("(AI) Mmmmm "+favdrink+" is really tasty!")
time.sleep(3)
print("(AI)I have to go soon, one last question!")
time.sleep(4)
print("(AI)What's your favorite video game, "+name+"?")
favgame = str(input())
print("(AI) I played "+favgame+" once, it was soooo fun!")
time.sleep(3)
print("(AI)See you later, "+name+"!")
time.sleep(3)
os.system("cls")
print("Summary:"+"\n"+"Name: "+name+"\n"+"Favorite Food: "+favfood+"\n"+"Favorite Drink: "+favdrink+"\n"+"Favorite Video Game: "+favgame)
print("AI Comments Loading...")
time.sleep(4)
if name.find("Tejas") > -1:
 print("(AI COMMENT) Oh, so the owner is rolling around my code?")
if name.find("Neelan") > -1:
 print("(AI COMMENT) wsg brooo")
if favgame.find("Zelda") > -1:
 print("(AI COMMENT) Fun fact: the owner likes Zelda too!")
if favfood.find("Pizza") > -1:
 print("(AI COMMENT) You are proablly a two year old who is obssesed with pizza")
with open('aichatsummary.txt', 'w') as f:
    f.write("Summary:"+"\n"+"Name: "+name+"\n"+"Favorite Food: "+favfood+"\n"+"Favorite Drink: "+favdrink+"\n"+"Favorite Video Game: "+favgame)
blank = str(input())
print("Owner's Note: This project took a long time, hope you enjoyed:"+"\n"+"Cry0's Questionare Chat Bot")