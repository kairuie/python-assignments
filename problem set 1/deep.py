answer = input("What is the answer to Great Question of Life, the Universe and Everything? ")

new = answer.lower()

print(new)

# match new:
#     case "42" | "fourty two" | "fourty-two":
#         print("Yes")
#     case _:
#         print("No")

if new == "42" or new == "fourty two" or new == "fourty-two":
    print("Yes")
else:
    print("No")