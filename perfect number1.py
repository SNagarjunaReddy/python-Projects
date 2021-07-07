number=int(input("enter your value : "))
value=1
Sum=0
while value<number:
    if number % value==0:
        Sum += value
    value +=1
if Sum == number:
    print(number,"is a perfect number")
else:
    print(number,"is not a perfect number")
