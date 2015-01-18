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



#### Third Approach:

s = 'azcbobobegghaklbobbobjfuboboo'
sub = 'bob'
def find(s, sub):
    counter = start = 0
    while True:
        start = s.find(sub, start) + 1
        if start > 0:
            counter+=1
        else:
            return counter
print find(s,'bob');


