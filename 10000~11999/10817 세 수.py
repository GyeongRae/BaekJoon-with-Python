A,B,C=map(int,input().split()) #세 정수 입력 split함수로 공백 기준 변수 저장
if(A>B):        # A>B 
    if(B>C):    # A>B>C일때 
        print(B)
    else:
        if(A>C): # A>C>B
            print(C)
        else: # C>A>B
            print(A)
else:
    if(B<C):    # C>B>A
        print(B)
    elif(A>C): # B>A>C
        print(A)
    else:    #B>C>A
        print(C)
