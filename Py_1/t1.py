char = 50
def check(s):
    global char
    c1 = [0] * char
    c2 = [0] * char
    
    n = len(s)
    if n ==1:
        return true
    
    i = 0; j = n-1
    while(i<j):
        c1[ord(s[i]) - ord('a')] +=1
        c1[ord(s[j]) - ord('a')] +=1
        
        i +=1; j -= 1
        
    for i in range(char):
        if c1[i] != c2[i]:
            return False
    return True

s = input("Enter string \t")

print("Yes" if check(s) else "No")