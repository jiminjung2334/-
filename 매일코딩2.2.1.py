def pig_latin():
    word = input("단어를 입력해주세요: ")
    result = ""
    if word[0] in 'aeiou':
        result = result + word + 'way'
        return result
    else:
        result = word[1:] + word[0] + 'ay'
        return result

print(pig_latin())