a=0
def  check(st):
    if st==a:
        print(a)

def d(str):
    for i in range(len(str)):
        check(str[i])
        print(str[i])   
        
        
str = input("String   : ")

d(str)

