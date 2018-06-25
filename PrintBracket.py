"""
Print Bracket Number :GFG 
Difficulty : easy
Lang :  python
"""


for r in range(0,int(input())):
    exp=input();
    i=1;
    for ch in exp:
        #print(ch)
        if ch=='(':
            print(i,end =" ");
            i=i+1;
        elif ch==')':
            i=i-1;
            print(i,end =" ");
            i=i+1;
    print("")
