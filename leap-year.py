x = int(input())
if x%400==0:
    print(x,"is leap year")
else:
    if( x%4==0 and x%100!=0):
        print(x,"is leap year")  
    else:
        print(x,"is not leap year")