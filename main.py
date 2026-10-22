# Trivia Game: pyTrivia
import datetime
import random
import threading
import time

print("Welcome! Let's play pyTrivia!")
# Menu Text
menText = "Menu: \n > Rules \n > Play \n > About \n"
Menu = input(menText)
t = 0
#Functions of Menu Options
while True:
  if Menu == "play" or Menu == "Play":
    while True:
      Level = input("\nPlease select a difficulty level: \n Easy (60) \n Medium (45) \n Hard (30) \n\n")
      if Level == "Easy (60)" or Level == "Easy" or Level == "Easy(60)" or Level == "easy":
        t = 60
        break
      if Level == "Medium (45)" or Level == "Medium" or Level == "Medium(45)" or Level == "medium":
        t = 45
        break
      if Level == "Hard (30)" or Level == "Hard" or Level == "Hard(30)" or Level == "hard":
        t = 30
        break
      else:
        print("Sorry, I didn't get that.")
        continue
    while True:
      Category = input("\nPlease select a category: \n Math \n Science \n History \n Music \n\n")
      if Category != "Math" and Category != "Science" and Category != "History" and Category != "Music":
        print("Sorry, I didn't get that.")
        continue
      else:
        break
    break
  elif Menu == "Rules" or Menu == "rules":
    print("\nRules: \n" + 
          "1. Select a difficulty mode (a time control in seconds) and a category. \n" +
          "2. In up to three attempts per question, try to answer all 5 questions correctly in the allotted time. \n" +
          "3. If all the questions are answered correctly, you have a chance to boost your score! \n" +
          "4. Lowercase single-word answers only. \n\n")
    Menu = input(menText)
  elif Menu == "about" or Menu == "About":
    print("\nAbout: \n" + "Trivia game by Preksha Shyamsukha for CS First Winter Project 2024. \n\n")
    Menu = input(menText)
  else:
    Menu = input("Sorry, I didn't get that. \n\n" + menText)

# Question Sets
MathQ = {
  "1. What is the sum of the numbers on the opposite sides of a die?": "seven",
  "2. What measurement of time is the same as 0.01 seconds?": "jiffy",
  "3. What number is twice the sum of its digits?": "eighteen",
  "4. What number was originally called a cipher?": "zero",
  "5. What is the proper name for the division bar in a fraction?": "vinculum"
}

ScienceQ = {
  "1. What is the name of the tallest grass on earth?" : "bamboo",
  "2. Which is the most abundant element in the universe?" : "hydrogen",
  "3. What is the study of mushrooms called?" : "mycology",
  "4. Does sound travel faster in the air or in water?" : "water",
  "5. What part(s) of the human body help(s) maintain balance?" : "ears"
}

HistoryQ = {
  "1. How many U.S. presidents have been assassinated?" : "four",
  "2. The ancient city of Rome was built on how many hills?" : "seven",
  "3. Fill in the blank: In 1957, humans launched the first ____ into orbit." : "satellite",
  "4. Fill in the blank: The 19th Amendment of the US Constitution guarantees ____ the right to vote." : "women",
  "5. What does demokratia (a concept introduced by Athenian leader Cleisthenes in 507 BC) translate to?" : "democracy"
}

MusicQ = {
  "1. What is Taylor Swift's favorite number?" : "thirteen",
  "2. Fill in the blank: The Weeknd's parents are Ethiopian ____." : "immigrants",
  "3. Cardi B had how many top ten singles at once on the Billboard Hot R&B/Hip Hop chart?" : "five",
  "4. Lana del Rey is a fan of what sport?" : "soccer",
  "5. Fill in the blank: Before becoming a famous rapper, Travis Scott began his music career as a ____." : "producer"
}

Score = 0
print("Score: ", Score)

stop = False
# Timer function
def clock(sec = 1):
  interval = 3
  while sec > -1:
    timer = datetime.timedelta(seconds = sec)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t", timer, end="\r")
    time.sleep(interval)
    sec -= interval
    global stop
    if stop:
      sec = 0
      print("Hooray! You have finished the questions!")
      break
  if not stop:
    stop = True
    print("Time's up! Better luck next time!")

# Quizzing function
def askQ():
  global stop
  subject = {}
  if Category == "Math":
    subject = MathQ
  if Category == "Science":
    subject = ScienceQ
  if Category == "History":
    subject = HistoryQ
  if Category == "Music":
    subject = MusicQ

  for item in subject:
    ask = input(item + "\n")
    print("You entered: " + ask)
    for i in range(3):
      if ask == subject[item]:
        print("Yay! This is the correct answer!")
        global Score
        Score += 50
        print("Score: ", Score)
        break
      else:
        if stop:
          return
        if i == 2:
          print("Wrong answer. You have run out of attempts. ")
          print("Correct answer: " + subject[item])
        else:
          ask = input("Wrong answer. Please try again. \n")
  stop = True

if __name__ == "__main__":
  thread1 = threading.Thread(target = clock, args = (t,))
  thread2 = threading.Thread(target = askQ)

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

#Die-rolling (Bonus)
if Score == 250:
  print("\nYou can now roll a die to boost your score!")
  faces = int(input("Enter the number of faces on the die (must be at least 2 faces but no more than 5): "))
  while True:
    if faces < 2 or faces > 5:
      faces = int(input("Please try again. Enter a number >= 2 or <= 5: "))
    else:
      break
  print("Rolling the die... ")
  roll = random.randint(1, faces)
  print(roll, "\n")
  Score += roll * 50
  print("You have gained", roll*50, "points.")
  print("Your final score: ", Score, "\n")
  print("Congratulations! You have finished the game!")