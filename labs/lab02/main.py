# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# Janay Camper 10/7/2026

# Print ot title
print() # prints an empty line
print("My Awesome Quiz on Python Concepts")
print() # prints an empty line
print("*" * 20) # print a line of 20 astericks

# Ask for the user's name
print()
username = input(" What's your name? ")
print(f"Hello, {username}!) # f-string format

# Ask if they want to take a quiz
print()
start_quiz = input(" Do you want to take my awesome quiz? Y/N ")
if start_quiz.upper() == "Y" : # this will make any lowercase an uppercase for comparrison
  print("Great Let's get stated!")
  # put our quiz questions all here indented
  # START OUR QUIZ QUESTIONs

  #Set our counter to 0
  counter = 0

  # Question 1
  q1 = int(input(" How would python solve 8 * 10? "))
  if q1 == 80: 
      # update my counter because they got the answer right
      counter += 1 # shorthand for counter = counter + 1
      print("Yes! You are correct. Python would solve this as 80.")
  else: #INCORRECT
    print("Sorry. That is not correct.")
  
  # Question 2
  print(" What is the function that we use to....?")
  print("  A -output()")
  print("  B -print()")
  print("  C -format()")
  print("  D - None of the above" )

  # Question 3

  # Question 4

  # Question 5

  # Ouput the score
  print("**** YOUR FINAL SCORE****")
  print(f"Your final score is: {counter}")

  # Givee them feedback on their overall score
  if counter == 5:
    print(" You are...")
  elif counter >= 3 and counter < 5:
    print("YAY")
  elif counter >= 1

