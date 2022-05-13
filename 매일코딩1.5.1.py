# 나중에 다시 보기
def hex_output():
    decnum = 0
    hexnum = input("숫자를 입력하시오: ")
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

hex_output()