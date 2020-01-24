#!/usr/bin/python3

# Create dictionary object
eng2deu = {'one': 'eins', 'two': 'zwie', 'three': 'drei' }

print(eng2deu)

# view elements of dictionary
print(eng2deu['one'])
print(eng2deu['three'])

#add and remove from dictionary
eng2deu.update({'four': 'vier'})
eng2deu.pop('two')

print(eng2deu)

#Show all keys and all values
print(eng2deu.keys())
print(eng2deu.values())




