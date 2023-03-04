from os import remove
from time import sleep
import pyperclip

f = open("bibino", "w+") 
f.write(" ") 
f.close()


meme = input("text: ")  
f = open("bibino", "a")
x = 0
for i in range(len(meme)):
    f.write("||" + meme[x] + "||")     
    x += 1
f.close()

f = open("bibino", "r")  
text = f.read()      
print(text)         
pyperclip.copy(text)
print("Copied automatically to clipboard!")
f.close()
sleep(1)
remove("bibino") 