def main():
    inTime = input("What time is it? ")
    newTime = convert(inTime)
    if  7 <= newTime <= 8:
        print("breakfast time")
    elif  12 <= newTime <= 13:
        print("lunch time")
    elif  18 <= newTime <= 19:
        print("dinner time")
    else:
        print("")



def convert(time):
    sTime = time.split(":")
    hours = float(sTime[0])
    minutes = float(sTime[1])/60
    fTime = hours + minutes
    return fTime

if __name__ == "__main__":
    main()