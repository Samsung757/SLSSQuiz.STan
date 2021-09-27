# Quiz Creation Activity

# Quiz has 5 questions the user will answer
# It will keep track of score and give a final result
import time
import random

congrats = ["Wow! You got that incredibly difficult question right! I'm so proud of you!",
                   "Oh! I can't believe you got that right! That was such a hard question!",
                   "Hmm... It seems that you're not as incompetent as I thought! I'll have to make harder questions next time!",
                   "So impressive!",
                   "You little tryhard.",
                   "Butbutbut... How could you have gotten such a difficult question right??"]

failures = ["Ha! I knew you would fail that one!",
                   "You're so incompetent you couldn't even solve this question? You don't even deserve to do my quiz.",
                   "Your mother would be so disappointed in you right now",
                   "Oh too bad, I'm sure you'll get the next one right. Actually, no I'm not, you little failure.",
                   "You're even worse than the last person who did this quiz. And Oscar did terribly.",
                   "Wow. So this is why your parents abandoned you as a child."]

score = 0

print ("Hi, I'm Fricking Quiz Bot!")
print ("I'll bother you with multiple annoying and easy questions while acting condescendingly if you get them wrong!")

# Question One
print ("Now for the first question:\n")
time.sleep(2)
print ("What is my name?")
answer1 = input().lower().strip(",.!?")

if answer1 == ("fricking quiz bot"):
    score = score + 1
    random_congrats = random.choice(congrats)
    print (f"{random_congrats}")
    time.sleep(2)


else:
    random_failure = random.choice(failures)
    print (f"{random_failure}")
    time.sleep(2)
    print("For your information, the correct answer was 'Fricking Quiz Bot', though I'm not sure your tiny brain can comprehend that.")
    time.sleep(2)

# Question Two
print ("Now for the second question:\n")
time.sleep(2)
print ("Factor 4x^2 - 18x + 18")

