greeting = input("Greeting: ")

greet = greeting.lower().lstrip()

if greet == "hello":
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")