user = input("Expression: ")

new = user.split()

x = new[0]
y = new[1]
z = new[2]

match y:
    case "+":
        print(round(float(x)+float(z), 1))
    case "-":
        print(round(float(x)-float(z), 1))
    case "*":
        print(round(float(x)*float(z), 1))
    case "/":
        print(round(float(x)/float(z), 1))
     
