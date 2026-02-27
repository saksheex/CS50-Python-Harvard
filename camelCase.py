
user=input("camelCase: ")
result = ""
for char in user:
    if char.isupper():          
        result += "_"           
        result += char.lower()  
    else:
        result += char          

print("snake_case:",result)
            