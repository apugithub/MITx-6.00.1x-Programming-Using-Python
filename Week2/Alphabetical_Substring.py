### 1st appraoch:

s = 'azcbobobegghakl'
def get_alphabetical_substring(s):
    offset = ''
    ans = ''
    temp = ''
    for letter in s:
        if letter >= offset:
            temp += letter
        else:
            temp = letter
        offset = letter
        if len(temp) > len(ans):
            ans = temp
    return ans
print get_alphabetical_substring(s) 



#### 2nd Approach:

from itertools import count
s = "jdisjsd sdpkds sdpsdsdfposodksdpfok "
maxSubstr = s[0:0]
for start in range(len(s)):
    for end in count(start + len(maxSubstr) + 1):
        substr = s[start:end]
        if len(substr) != (end - start):
            break
        if sorted(substr) == list(substr):
            maxSubstr = substr
print "Longest substring in alphabetical order is: " + str(maxSubstr)


#### 3rd Approach:

s = "azcbobobegghakl"
def solve(strs):
    maxx = ''
    for i in xrange(len(strs)):
        for j in xrange(i+1, len(strs)):
            q = strs[0]
            s = strs[i:j+1]
            if ''.join(sorted(s)) == s:
                maxx = max(maxx, s, key=len)
            else:
                break
    if maxx == '' :
        return q
    else:
        return maxx;
print solve(s)











