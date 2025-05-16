# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():

    letter = input("Enter a single letter: ").lower()
    # user inputs a letter and with the lower() method, it will automatically lowercase it. 
    vowels = ['a', 'e', 'i', 'o', 'u']
    # list of vowels

    if len(letter) == 1 and letter in vowels:  
        print(f"The letter {letter} is a vowel.")
    # check if the letter is in the the list. The in keyword literally means that check in container. and also check if a single character has been inputted. 

    elif len(letter) == 1 and letter.isalpha():
        print(f"The letter {letter} is a consonant.")
    # if letter is not in the list, it then checks if its anyother letter with the help of the .isalpha method. 
    #It returns true if the character is in the alphabet. Handy method instead of listing the entire alphabet out 
    else:
        print("Invalid input. Please enter a single letter.")

# Call the function
check_letter()

#note to self: print(f -> you put the f before the string , that you can use a variables directly into the string. 



# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    age = int(input("Please enter your age: "))
    voting_age = 18 #min age for voting

    if age < 0:
        print("You really can't be of a negative age")
    elif age >= voting_age:
        print("You can vote!")
    else:
        print("You are to young to vote")

# Call the function
check_voting_eligibility()

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
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
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    human_age = int(input("Please enter your dog's age in human age: "))  # Get the dog's age as an integer

    if human_age < 0:
        print("Invalid input. Pretty sure dog's age cannot be negative.")
    elif human_age <= 2: 
        dog_years = human_age * 10  # First two years count as 10 dog years each, so any age between 1 and 2 ( coun't the decimals)
        print(f"Your dog's age in dog years is {dog_years}.")
    else:
        # First two years count as 10 dog years each, and the rest count as 7 dog years
        dog_years = (2 * 10) +((human_age - 2) * 7)
        print(f"Your dog's age in dog years is {dog_years}.")

# Call the function
# calculate_dog_years()

# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
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
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    is_cold = input("Is it cold today? : yes/no ")
    is_raining = input("Is it raining today? : yes/no ")

    if is_cold  == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and  is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold  == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

# Call the function
weather_advice()


# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Your control flow logic goes here
    user_month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day = int(input("Enter the day of the month: "))

#- Dec 21 - Mar 19: Winter > This means
# dec 21 to 31st OR Jan and feb OR March 19. Because its covering a part of Dec and March, while the entire jan and feb is covered
# we don't care what day in jab and feb because its still winter 
    if (user_month == "Dec" and day >= 21)  or (user_month in ("Jan", "Feb")) or (user_month == "Mar" and day <= 19):
        print(f"{user_month} {day} is in Winter.")

#- Mar 20 - Jun 20: Covers March 20th to april and may  to Jan 20
    elif (user_month == "Mar" and day >= 20) or user_month in ("Apr", "May") or (user_month == "Jun" and day <= 20):
        print(f"{user_month} {day} is in Spring.")

# - Jun 21 - Sep 21: Summer
    elif (user_month == "Jun" and day >= 21) or user_month in ("Jul", "Aug") or (user_month == "Sep" and day <= 21):
        print(f"{user_month} {day} is in Summer.")

#- Sep 22 - Dec 20: Fall
    elif (user_month == "Sep" and day >= 22) or user_month in ("Oct", "Nov") or (user_month == "Dec" and day <= 20):
        print(f"{user_month} {day} is in Fall.")
    else: 
        print("Make sure you the month like: Dec,  otherwise its not going to work")

# Not sure if this is the best soultion considering the long statments, but using the OR logic does help condense the statements and also helps combine the logic alot better.     

# Call the function
determine_season()