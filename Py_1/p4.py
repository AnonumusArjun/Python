def en(str):
    key = 9

    enc = ""

    for c in str:
        if not any(c.isdigit()):
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            
            new_index = (c_index + key)%26
            new_unicode = new_index +ord("A")
            new_char = chr(new_unicode)
            
            enc = enc +new_char
            
        else:
        
            enc += c

    
    print(enc)


str = input("Enter string...")

for i in range(len(str)):
    en(str[i])