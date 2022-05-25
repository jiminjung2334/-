def strsort(word):
    result = ''
    word = sorted(word)
    for i in word:
        result += i
    return result

word = input()
print(strsort(word))

