valid_passphrases = 0
with open('day-04/input', 'r') as file:
    for line in file:
        passphrase = line.split()
        if len(passphrase) == len(set(passphrase)):
            valid_passphrases += 1
print(valid_passphrases)