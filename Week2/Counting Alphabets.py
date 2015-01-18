# First Programe:

s= 'abnghdfteryt'
def count_vowels(s):
    vowels = 'aeiou'
    counter = 0
    for vowel in s:
        if vowel in vowels:
            counter += 1
    return counter
print count_vowels(s)


# Second Program:

word = str(raw_input("Enter a word: "));
numVowel = 0
for vowel in word:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        numVowel += 1
print("Number of vowels: " + str(numVowel))


### Third approach:

s = 'azcbobobegghaklbobbobjfuboboo'
counter = 0;
counter = s.count('a') + s.count('e') +s.count('i') +s.count('o') +s.count('u');
print counter;


