# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
  # Your code goes here. Remember to indent!
  python_is_fun = True
  if python_is_fun:
    print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.
# ref: https://pynative.com/python-check-user-input-is-number-or-string/

def check_letter():
  letter = input("enter a letter: ")
  lower = letter.lower()
  vowels = 'a','e','i','o','u'
  consonant = 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
  
  if lower in vowels:
    print(f"The letter {letter} is a vowel")
  elif lower in consonant:
    print(f"The letter {letter} is not a vowel")
  else:
    try:
      letter = int(letter)
      print(f"{letter} is a number not a letter")
    except ValueError:
      print(f"{letter} is not a letter nor a number")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
  age = input("what is your age? ")
  voting_age = 18

  try:
    age= int(age)
    if age>voting_age:
      print("you're old enough to vote")
    elif age<voting_age and age>0:
      print("you're not old enough to vote")
    elif age<0:
      print("your age can't be below 0")
    else:
      print("something wen't wrong")
  except ValueError:
    print("what you entered is not a number")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
  age = input("What's your dog age?")
  dog_age=0
  counter=3

  try:
    age = int(age)
    if age==0:
      print("too young to count")
    elif age<0:
      print("age can't be below 0")
    else:
      if age>=1:
        dog_age+=10
      if age>=2:
        dog_age+=10
      while counter<=age:
        counter+=1
        dog_age+=7
      print(f"The dog's age in dog years is {dog_age}")
  except ValueError:
    print("this is not a number")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
  cold = input("is it cold? type yes or no, y or n only: ").lower()
  rain = input("is it raining? type yes or no, y or n only: ").lower()
  if cold == 'yes' or cold == 'y':
    if rain == 'yes' or rain == 'y':
      print("Wear a waterproof coat.")
    elif rain == 'no' or rain == 'n':
      print("Wear a warm coat.")
    else:
      print("you didn't say if it's raining or not?")
  elif cold == 'no' or cold == 'n':
    if rain == 'yes' or rain == 'y':
      print("Carry an umbrella.")
    elif rain == 'no' or rain == 'n':
      print("Wear light clothing.")
    else:
      print("you didn't say if it's raining or not?")
  else:
    print("you didn't say if it's cold or not?")
  
# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def out_of_range():
  print("the number is out of range")

def result(mon, day, season):
  print(f"{mon} {day} is in {season}")

def determine_season():
  months= 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec' 
  months_with_31 = 'jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'
  
  month = input("Enter the month of the year (Jan - Dec):")
  lower = month.lower()
  if lower in months:
    day = input("Enter the day of the month:")
    try:
      day = int(day)
      if lower in months_with_31:
        if day>31 or day<1:
          out_of_range()
          exit()
      elif lower == 'feb' and day>28 or day<1:
        out_of_range()
        exit()
      else:
        if day>30 or day<1:
          out_of_range()
          exit()
      
      if (lower=='jan' or lower=='feb') or (lower=='dec' and day>=21) or (lower=='mar' and day<=19):
        result(month, day, 'Winter')
      
      if (lower=='apr') or (lower=='may') or (lower=='mar' and day>=20) or (lower=='jun' and day<=20):
        result(month, day, 'Spring')

      if (lower=='jul') or (lower=='aug') or (lower=='jun' and day>=21) or (lower=='sep' and day<=21):
        result(month, day, 'Summer')

      if (lower=='oct') or (lower=='nov') or (lower=='sep' and day>=22) or (lower=='dec' and day<=20):
        result(month, day, 'Fall')

    except ValueError:
      print("what you entered is not a number")
  else:
    print("This is not a month, or it's written in the wrong format")

# Call the function
determine_season()
