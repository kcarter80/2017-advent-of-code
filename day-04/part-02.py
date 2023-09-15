# returns a dictionary of the count of letters in a word
# e.g. "hello" would return { h: 1, e: 1, l: 2, o: 1}
def letter_counts(word):
    counts_dict = {}
    for char in word:
        if char not in counts_dict:
            counts_dict[char] = 1
        else:
            counts_dict[char] += 1
    return counts_dict

valid_passphrases = 0
with open('day-04/input', 'r') as file:
    for line in file:
        passphrase = line.split()
        counts = []
        for word in passphrase:
            counts.append(letter_counts(word))
        # in python dictionaries are unhashable and cannot be added to a set, so frozenset are used
        frozenset_list = [frozenset(d.items()) for d in counts]
        # if the letter_counts for each word are different (i.e. no duplicates, so same length)
        if len(counts) == len(set(frozenset_list)):
            valid_passphrases += 1
print(valid_passphrases)