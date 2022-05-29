import operator

PEOPLE = [{'first' : 'Reuven', 'last' : 'Lerner'}, {'first' : 'Donald', 'last' : 'Trump'}, {'first' : 'Vladimir', 'last' : 'Putin'}]

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key = operator.itemgetter('last', 'first'))

print(alphabetize_names(PEOPLE))