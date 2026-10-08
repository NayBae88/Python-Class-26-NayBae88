# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# Janay Camper 10/7/2026

# Print out title 
print() #prints an empty line
print("Nay's Awesome Python Quiz")
print() # prints an empty line
print("* " * 20) # print a line of 20 astericks

# Ask for the user's name
print()
username = input(" What's your name? ")
print(f"Hello, {username}!") # f-string format

# Ask if they want to take a quiz
print()
start_quiz = input(" Do you want to take my awesome quiz? Y/N ")
if start_quiz.upper() == "Y" : # this will make any lowercase input into an uppercase for comparison
  print("Great Let's get stated!")
  # put our quiz questions here all indented
  # START OUR QUIZ QUESTIONS

  # Set counter to 0
  counter = 0

  # Question 1
  print()
  print("*** Question 1 ***")
  print()
  q1 = int(input(" How would Python solve 8 * 10? "))
  if q1 == 80: # CORRECT
      # update my counter because they got the answer right
      counter += 1 # shorthand for counter = counter + 1
      print("Yes! You are correct. Python would solve this as 80.")
  else: #INCORRECT
    print("Sorry. That is not correct.")

  # Question 2
  print()
  print("*** Question 2 ***")
  print()
  print(" What is the function that we use to display text on the screen?")
  print("  A - output()")
  print("  B - print()")
  print("  C - format()")
  print("  D - None of the above")
  q2 = input("Your Answer - Choose A/B/C/D: ")
  if q2.upper() == "B":
     # update my counter because they got the answer right
       counter += 1 # shorthand for counter = counter + 1
       print("Yes! You are correct. Python would use the print() function to display text on the screen.")
  else: #INCORRECT
         print("Sorry. That is not correct.")

  # Question 3
  print()
  print("*** Question 3 ***")
  print()

  # Question 4
  print()
  print("*** Question 4 ***")
  print()

  # Question 5
  print()
  print("*** Question 5 ***")
  print()

  # Ouput the score
  print("* * * * YOUR FINAL SCORE * * * *")
  print(f"Way to go {username}! Your final score is: {counter} out of 5. ")

  # Give them feedback on their overall score
  if counter == 5:
    print("PERFECT SCORE! You got 5 out of 5! Okayyy Python genius! ")
  elif counter >= 3 and counter < 5:
    print("You're on the right track! Keep going, Keep Coding")
  elif counter >= 1 and counter < 3:
     print("Keep at it, you've got potential! Practice makes progress. ")
  else:
     print("So maybe this isn't your niche, but it won't hurt to keep trying!")

elif start_quiz.upper() == "N":
    print("Sorry, maybe next time!")

else: #if they type anything else tell them it is invalid
   print("Sorry. That is an invalid response. Try again.")

# Print a farewell message
print("Thank you for your time and have an awesome day!")



print("Thank you for your time and have an awesome day!")
