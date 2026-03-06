import random

def get_int():
    while True:
        try:
            user = int(input("Level: "))
            if user > 0:
             return user
        except ValueError:
            pass

user_in = get_int()  
r = random.randint(a=1,b=user_in)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < r:
            print("Too Small!")
        elif guess > r:
            print("Too Large!")
        elif guess == r:
            print("Just right!")
            break
    except ValueError:
        pass