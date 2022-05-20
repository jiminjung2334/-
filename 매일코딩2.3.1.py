def pl_sentence(input):
    output = str()
    for word in input.split():
        if word[0] in 'aeiou':
            output = output + word + 'way'
        else:
            output = output + word[1:] + word[0] + 'ay'
    print(output)

input = ("this is a test")
(pl_sentence(input))
