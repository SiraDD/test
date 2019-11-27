def fibo(number):
  number1=1
  number2=1
  for i in range(number):
    print(number2)
    temp=number2
    number2 += number1
    number1 = temp
