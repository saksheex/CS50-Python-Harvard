


def make_lower(a):
    if any(char.isupper() for char in a):
        print("Capital letter found, converting to lowercase\n")
        return a.lower()
    else:
        print("You are good to go, no capitals found!\n")
        return a

text = input("Enter your inputs:\n ")
result = make_lower(text)
print("Final Version after review:", result)


