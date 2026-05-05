

possible=[32,32,32,32]
keys=0
while 1:
   
    for a in range(0,keys+1):
        print(chr(possible[a]),end="")
    print("")
    p=possible[0]
    p=p+1
    possible[0]=p
    if p>127:
        possible[0]=32
        if keys==0:
             keys=1
        p=possible[1]
        p=p+1
        possible[1]=p
        if p>127:
            possible[1]=32
            if keys==1:
                keys=2
            p=possible[2]
            p=p+1
            possible[2]=p
            if p>127:
                possible[2]=32
                if keys==2:
                    keys=3
                p=possible[3]
                p=p+1
                possible[3]=p