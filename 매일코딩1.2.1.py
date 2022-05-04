import random

def guessing_game():
    number = random.randint(0, 100)
    guess = int(input("숫자를 맞춰보세요: "))
    while number != guess:
        if (guess > number):
            print("너무 큽니다")
        if (guess < number):
            print("너무 작습니다")
        guess = int(input("숫자를 맞춰보세요: "))
    print("정답입니다")

guessing_game()

"""
<더 나은 코드 - while문 부분 수정>
while True:
    guess = int(input("숫자를 맞춰보세요: "))
    if guess == number:
        print("정답입니다")
        break
"""    
