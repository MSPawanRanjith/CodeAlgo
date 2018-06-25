"""
Print Bracket Number :GFG 
Difficulty : easy
Lang :  python
"""


for r in range(0,int(input())):
    exp=input();
    i=1;
    list=[]
    for ch in exp:
        #print(ch)
        if ch=='(':
            print(i,end=" ");
            list.append(i)
            i=i+1;
        elif ch==')':
            print(list.pop(-1), end=" ")
    print("")
