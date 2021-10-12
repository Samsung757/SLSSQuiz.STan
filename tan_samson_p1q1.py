# Quiz Creation Activity

# Quiz has 5 questions the user will answer
# It will keep track of score and give a final result
import random
import time
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
print ("Factor -3x^2 - x + 4")
answer2 = input().lower().strip(",.!?")

if answer2 == ("-(3x-4)(x-1)"):
    score = score + 1
    random_congrats = random.choice(congrats)
    print (f"{random_congrats}")
    time.sleep(2)


else:
    random_failure = random.choice(failures)
    print (f"{random_failure}")
    time.sleep(2)
    print("For your information, the correct answer was '-(3x-4)(x-1)'. Go back to math class.")
    time.sleep(2)

    # Question Three
print("Now for the third question:\n")
time.sleep(2)
print("What is Oscar's name?")
answer3 = input().lower().strip(",.!?")

if answer3 == ("oscar"):
    score = score + 1
    print("Wow! How did you get that question right?? ")
    time.sleep(2)


else:

    print(f"You know what? I'm just ending the quiz there. How astoundingly stup- Sigh. Your score was {score}. I'm so disappointed in you. ")
    time.sleep(2)
    quit()

# Question Four
print ("Now for the fourth question:\n")
time.sleep(2)
print ("Am I cool?")
answer4 = input().lower().strip(",.!?")

if answer4 == ("yes"):
    score = score + 1
    random_congrats = random.choice(congrats)
    print (f"{random_congrats}")
    time.sleep(2)


else:
    print("I am obviously so cool. In fact, I'm so much cooler than you that you probably just didn't even notice.")
    time.sleep(2)



# Question Five
print("Now for the fifth question:\n")
time.sleep(2)
print("Is Luigi Mario's brother?")
answer5 = input().lower().strip(",.!?")

if answer5 == ("yes"):
    score = score + 1
    random_congrats = random.choice(congrats)
    print(f"{random_congrats}")
    time.sleep(5)



else:
    random_failure = random.choice(failures)
    print(f"{random_failure}")
    time.sleep(2)
    print("Yes. He is. How dumb are you?")
    time.sleep(5)



print("Ok, that's it for the quiz!")
print("I hope you didn't enjoy that")
print(f"Your score was {score}.")
print(f"Your percentage is {(score / 5) * 100}%")


if score == 5:
     print ("Wow! Even though you're astoundingly stupid, you managed to get 100%! Great job.")

elif score >  2:
     print ("Eh, that's ok.")

elif score > 1:
    print("You little useless idiot with no IQ. Go back to whatever preschool you crawled out of")

else:
    print("I don't even know what to say. Buffoon.")

