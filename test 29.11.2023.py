with open ("kompresia_obrazka_1.txt", "r") as f:
    lines=f.readlines()
def spracuj_riadok(currline):
    curr=""
    resline=""
    if currline[0]=="1":
        resline="0 "
    safety=0
    while (currline[safety]=="0" or currline[safety]=="1") and safety<1000:
        if currline[safety]=="0":
            if curr=="":
                curr="0"
                currnum=1
            elif curr=="0":
                currnum+=1
            else:
                resline=(resline+str(currnum)+" ")
                curr="0"
                currnum=1
        elif currline[safety]=="1":
            if curr=="":
                curr="1"
                currnum=0
            elif curr=="1":
                currnum+=1
            else:
                resline=(resline+str(currnum)+" ")
                curr="1"
                currnum=1
        else:
            break
        safety+=1
    if safety==1000: print("safety overload")
    return resline

with open('kompresia_obrazka_vystup.txt', 'w') as f:
    f.write(lines[0])
    for i in range(len(lines)-1):
        temp=spracuj_riadok(lines[i+1])
        f.write(temp+"\n")