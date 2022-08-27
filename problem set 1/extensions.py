file = input("File name: ")

file.lower()

processed = file.split(".")

processed.append(" ")

match processed[1]:
    case "gif" | "jpg" | "jpeg" | "png":
        print("image/"+str(processed[1]))
    case "pdf" | "zip":
        print("application/"+str(processed[1]))
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")