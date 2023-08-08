money = int(input("請輸入價格"))
if (money>=10000):
    if(money>=100000):
        print(money*0.75,end ="元")
    elif(money>=50000):
        print(money*0.7,end ="元")
    elif (money>=30000):
        print(money*0.8,end = '元')
    else:
        print(money*0.95,end = '元')
else:
    print(money,end ='元')