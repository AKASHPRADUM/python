import random
n = random.randrange(1,100)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Guess Something High.")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Guess Something Lower than this.")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")