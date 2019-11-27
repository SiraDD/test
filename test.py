def fibo(number):
    number1=0
    number2=1
    for i in range(number):
        temp=number2
        number2 += number1
        number1 = temp
        print(number2/number1)
