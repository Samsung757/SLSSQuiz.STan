# Quiz Creation Activity

# Quiz has 5 questions the user will answer
# It will keep track of score and give a final result
import time
import random

random_congrats = ["Wow! You got that incredibly difficult question right! I'm so proud of you!",
                   "Oh! I can't believe you got that right! That was such a hard question!",
                   "Hmm... It seems that you're not as incompetent as I thought! I'll have to make harder questions next time!",
                   "So impressive!",
                   "You little tryhard.",
                   "Butbutbut... How could you have gotten such a difficult question right??"]

random_failures = ["Ha! I knew you would fail that one!",
                   "You're so incompetent you couldn't even solve this question? You don't even deserve to do my quiz.",
                   "Your mother would be so disappointed in you right now",
                   "Oh too bad, I'm sure you'll get the next one right. Actually, no I'm not, you little failure.",
                   ]

score = 1

print ("Hi, I'm Fricking Quiz Bot!")
print ("I'll bother you with multiple annoying and easy questions while acting condescendingly if you get them wrong!")
print ("Now for the first question:\n")
time.sleep(2)
print ("What is my name?")
answer1 = input().lower().strip(",.!?")

if answer1 == ("fricking quiz bot"):
    score = score + 1
