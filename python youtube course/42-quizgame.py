#------------------------------------ timestamp: 3:31:09 almost done w this
def new_game():
  
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print("-------------------------------")
    print(key)
    for i in options[question_num-1]:
      print(i)
    guess = input("Enter (A,B,C, or D): ")
    guess = guess.upper()
    guesses.append(guess)

    correct_guesses += check_answer(questions.get(key),guess)
    question_num += 1

  display_score(correct_guesses, guesses)

#------------------------------------
def check_answer(answer, guess):
  if answer == guess:
    print("Correct!")
    return 1
  else:
    print("Wrong!")
    return 0
#------------------------------------
def display_score(correct_guesses, guesses):
  print("------------------")
  print("Results")
  print("------------------")
  print("Answers: ",end=" ")
  for i in questions:
    print(questions.get(i), end=" ")
  print()
  
  print("Guesses: ",end="")
  for i in guesses:
    print(i, end="")
  print()

  score = int((correct_guesses/len(questions)) * 100)
  print("Your score is "+str(score)+" percent!")
#------------------------------------
def play_again():
  response = input("Do you want to play again? (yes or no?): ")
  response = response.upper()

  if response == "YES":
    return True
  else: 
    return False
#------------------------------------

questions = {
  "What's your name?: ": "A",
  "How old are you?: ": "C",
  "How many grams are in a kilogram?: ": "B",
  "Do you think you passed this quiz?: ": "B"
}

options = [["A. Nick","B. Chris","C. Zack","D. Rosseau"],["A. 13","B. 22","C. 23","D. 24"],["A. 1001","B. 1002","C. 1003","D. 1000"],
           ["A. Prolly not","B. Um, yuh","C. Who do you think you're talking to??","D. Lemme guess..... no"]]


new_game()

while play_again():
    new_game

print("Byeeeee")
