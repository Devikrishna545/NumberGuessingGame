import random

def generateRandomNumber():
    random_number = random.randint(1,100)
    return random_number

def giveHint(guess_number,secret_number):
     if guess_number < (secret_number - 10) or guess_number>(secret_number + 10):
         return "Cold"
     elif guess_number == secret_number:
         return "Right"
     else :
         return "Hot"    

def getSecretNumber():
    secret_number = generateRandomNumber()
    
    while True:
        guess_number = int(input("Please enter your guessed number:"))
        hint = giveHint(guess_number,secret_number)
        if hint == "Right":
            print(f"You guessed right!, the secret number is {secret_number}")
            break
        else:            
            print(hint)      


if __name__ == '__main__':
    getSecretNumber()
