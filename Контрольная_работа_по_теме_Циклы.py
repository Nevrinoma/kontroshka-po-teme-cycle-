from random import*
                                                         #1
#n=" "
#while type(n)!=int or n<1 or n>9:
#    try:
#        n=int(input("Введите число от 1 до 9 >>> "))
#    except TypeError:
#        print=("Введите число от 1 до 9 >>> ")
#for i in range(n):
#    print("(\_/)   ", end=" ")
#print()
#for i in range(n):
#    print("(o o)   ", end=" ")
#print()
#for i in range(n):
#    print("/ | \*  ", end=" ")



                                                       #2

#l=int(input("Введите число до которого хотите посчитать сумму >>> "))
#summ=0
#for i in range(1,l+1):
#    summ=i+summ
#print(f"Сумма чисел от нуля до числа {l} = {summ}")

                                                     #3
#number1=1
#number2=randint(0,100)
#tries=0
#print(number2)
#while number1!=number2:
#    number1=int(input("Введите число от 0 до 100==> "))
#    while number1>100 or number1<0:
#        try:
#            number1=int(input("Введите число от 0 до 100==> "))
#        except:
#            ValueError
#    if number1==number2:
#        tries+=1
#        print(f"Вы угадали число с {tries} попытки!")
#        break
#    elif number2>number1:
#        print(f"Число больше, чем {number1}")
#        tries+=1
#    elif tries==9:
#        print("У вас больше нет попыток(их было 10), загаданое число было ",number2)
#        break
#    else:
#        print(f"Число меньше, чем {number1}")
#        tries+=1



                                                   #4
#n2=0
#n1=int(input("Введите число которое хотите перевернуть: "))
#while n1>0:
#    digit = n1 % 10
#    n1 = n1 // 10
#    n2 = n2 * 10
#    n2 = n2 + digit  
 
#print(f"Вот такое число получилось >>> {n2}")
#
                                                    #5

#number=int(input("Введите число у которого нужно найти сумму и произведение цифр >>> "))
#summ=0
#proiz=1
#while number>0:
#    summ+=number%10
#    proiz*=number%10
#    number=number//10
#print(f"Сумма >>> {summ}")
#print(f"Произведение >>> {proiz}")
