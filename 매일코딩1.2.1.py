import random

def guessing_game():
    number = random.randint(0, 100)
    
    for i in range(3):
        guess = int(input("숫자를 맞춰보세요: "))   
        if (guess > number):
            print("너무 큽니다")
        elif (guess < number):
            print("너무 작습니다")
        elif (guess == number):
            print("정답입니다")
    print("맞히지 못했습니다")
    
guessing_game()

"""
<더 나은 코드 - while문 부분 수정>
while True:
    guess = int(input("숫자를 맞춰보세요: "))
    if guess == number:
        print("정답입니다")
        break
"""    
