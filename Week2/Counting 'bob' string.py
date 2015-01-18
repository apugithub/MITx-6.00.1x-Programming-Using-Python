### First programe:

s = 'azcbobobegghaklbobbobjfuboboo'
def counting_bobs(s):
    pattern = 'bob'
    index = 0
    counter = 0
    for letter in s:
        if letter == 'b':
            if s.find(pattern, index, index + 3) != -1:
                counter += 1
        index += 1
    return counter
print ("Number of times bob occurs is:"),
print  counting_bobs(s)



#### Second programe:

s = 'azcbobobegghaklbobbobjfuboboo'
countBob = 0
print countBob
for i in range(len(s)):
    if s[i:].startswith('bob'):
        countBob += 1
print("Number of times bob occurs is: ") + str(countBob)
