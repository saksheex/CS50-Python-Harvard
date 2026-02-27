employees_greetings = input("Greetings: ").strip().casefold()
if employees_greetings.startswith("hello"):
   print("$0")  
elif employees_greetings.startswith("h"):
    print("$20")
else:
    print("$100")