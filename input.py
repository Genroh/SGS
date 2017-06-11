# vim:fileencoding=utf-8

while(True):
    end = input("Would you continue? (Y/n) > ")
    if(end == 'Y' or end == 'y'):
        print("Ok.")
    elif(end == 'N' or end == 'n'):
        print("Bye bye!")
        break
    else:
        print("Input Y or n.")
        continue

    tmp = ""
    lst = []

    tmp = input("Input Team Number. (0 or 2-7) > ")
    if(int(tmp) != 0 and (int(tmp) < 2 or int(tmp) > 7) or tmp.isdigit() == False):
        print("Invalid input:Team")
        continue
    lst.append(tmp)

    tmp = input("Input Member Number. (1-5(or0,6)) > ")
    if(int(tmp) < 0 or int(tmp) > 6):
        print("Invalid input:Member")
        continue
    lst.append(tmp)

    tmp = input("Input HP. > ")
    if(int(tmp) < 1 or tmp.isdigit() == False):
        print("Invalid input:HP")
        continue 
    lst.append(tmp)

    tmp = input("Input ATK. > ")
    if(int(tmp) < 1 or tmp.isdigit() == False):
        print("Invalid input:ATK")
        continue
    lst.append(tmp)

    tmp = input("Input 収束数. > ")
    if(int(tmp) < 0 or tmp.isdigit() == False):
        print("Invalid input:収束数")
        continue
    lst.append(tmp)

    tmp = input("Input Rarelity. (S/U/E) > ")
    if(tmp == "S" or tmp == "s"):
        lst.append("SR")
    elif(tmp == "U" or tmp == "u"):
        lst.append("UR")
    elif(tmp == "E" or tmp == "t"):
        lst.append("EXR")
    else:
        print("Invalid input:Rarelity.")
        continue

    tmp = input("Input Name. > ")
    lst.append(tmp)

    tmp = ""
    for i in lst:
        tmp += i + ','
    tmp = tmp[:-1]
    print(tmp)

    file_object = open("memoca.csv", "a")
    file_object.write(tmp)
    file_object.write("\n")
    file_object.flush()
    file_object.close()

