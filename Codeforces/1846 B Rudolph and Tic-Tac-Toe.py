for i in range(int(input())):
    r1=input()
    r2=input()
    r3=input()
    if r1[0]==r1[1]==r1[2] and "." not in r1:
        print(r1[0])
    elif r2[0]==r2[1]==r2[2] and "." not in r2:
        print(r2[0])
    elif r3[0]==r3[1]==r3[2] and "." not in r3:
        print(r3[0])
    elif r1[0]==r2[0]==r3[0] and r1[0]!=".":
        print(r1[0])
    elif r1[1]==r2[1]==r3[1] and r1[1]!=".":
        print(r1[1])
    elif r1[2]==r2[2]==r3[2] and r1[2]!=".":
        print(r1[2])
    elif r1[0]==r2[1]==r3[2] and r1[0]!=".":
        print(r1[0])
    elif r1[2]==r2[1]==r3[0] and r1[2]!=".":
        print(r1[2])
    else:
        print("DRAW")