import random

top_range = input("Type a number: ")

if top_range.isdigit():
   top_range = int(top_range)

   if top_range <=0:
      print("Please type a number larger than 0 next time.")
      quit()

random_number = random.randint(0,top_range)

guesses = 1 #How many times user tried to guess

while True:
    user_guess = input("Make a guess: ")
   
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number larger than 0 next time.")
        continue

    if user_guess == random_number:
        print("You got it! ",guesses," times you tried to find")
        break
    elif user_guess > random_number:
        print("You were above the number! ")
    else:
        print("You were below the number!")    
         
    guesses +=1


