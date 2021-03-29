import random
secret_number = random.randint(1,1000)

guess = int (input("Guess number: "))

if guess > secret_number:
    print("That's too high, try again")
elif guess < secret_number: 
    print("This is too low, try again")
else:
    print("Correct")
    print("The secret number is ",secret_number)

low = 1
high = 1000
guess = (low+high)//2
while guess != secret_number:
    guess = (low+high)//2
    print("The computer takes a guess...", guess)
    if guess > secret_number:
        high = guess
    elif guess < secret_number:
        low = guess + 1
    if guess == secret_number:
        print("The computer guessed", guess, "and it's correct!")
        