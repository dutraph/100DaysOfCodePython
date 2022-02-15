numb_alphabet = {
 1: 'a',
 2: 'b',
 3: 'c'
}


# Add value e to a dictionary
numb_alphabet[4] = 'd'

# Wipe an existing dictionary
#numb_alphabet = {}

# Edit an item in a dictionary
numb_alphabet[1] = 'j'
print(numb_alphabet)

# Loop through a dictionary
for key in numb_alphabet:
    print(key, end=': ')
    print(numb_alphabet[key])