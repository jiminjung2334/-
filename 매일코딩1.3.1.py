def mysum(*numbers):
    output = 0
    for i in numbers:
        output += i
    return output

print(mysum(10, 20, 30, 40))