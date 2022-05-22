def ubbi_dubbi(word):
    result = str()
    for i in word:
        if i in 'aeiou':
            result += 'ub' + i
        else:
            result += i
    return result

word = input()
print(ubbi_dubbi(word))
