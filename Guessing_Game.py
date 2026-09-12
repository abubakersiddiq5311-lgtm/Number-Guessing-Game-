import random
while True:
   print("="*40)
   print("Numbers Hunter Game")
   print("="*40)
   print("\nWelcome to Number Hunter")
   print("I have selected a secret number ranging from 1 to 10.")
   print("Your goal is to guess that number.")
   print("If you guess Correctly then you will have won.")
   print("If You guessed wrong then i will hint you to whether go higher or lower.\n")
   print("Be Aware : You have totally four attempts to guess\n")
   secret_number = random.randint(1,10)
   won = False

   for attempt in range(1,5):
      guess = int(input(f"Enter your Guess: "))
      if guess == secret_number:
         print("\nCORRECT! YOU WON!")
         won = True
         break
      elif guess > secret_number:
         print("WRONG!")
         print("Hint: Go Lower")
      elif guess < secret_number: 
         print("Wrong!")
         print("Hint: Go Higher")

   if guess != secret_number:
      print("GAME OVER!")
      print(f"The Secret Number was: {secret_number}\n\n")

   again=input("Do you want to continue the game (yes/no):")
   if again=="no":
      print("Thanks for playing!")
      break
   elif again=="yes":
      print("\n Starting new game....")
   else:
      print("Invalid Choice!")
      break