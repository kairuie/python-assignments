def main():
    string = input("camelCase: ")
    print(convert_string(string))


def convert_string(string):
    new = ""
    for s in range(len(string)):
        if string[s].isupper():
            lwr = string[s].lower()
            rep = string.replace(string[s], lwr)
            new = rep[:s] + "_" + rep[s:]
            string = new
    return new
        
        

        
main()


