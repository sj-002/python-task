    #1 SQUARE OF LIST
# numbers=list(map(int,input('enter number:').split()))
# square=list(map(lambda x:x**2,numbers))
# print('square of the list is:',square)

    #3 ADD 10 TO EACH NUMBER
# number=[1,2,3,4,5]
# add=list(map(lambda x:x+10,number))
# print('added 10 to each item in list:',add)

    #4 DOUBLE THE NUMBER
# number=list(map(int,input('enter number: ').split()))
# double=list(map(lambda x:x*2,number))
# print('twice of a number is:',double)

    #5 CAPITALIZE 
# s=['hi','buddy']
# caps=list(map(lambda x:x.capitalize(),s))
# print(caps)

    #6 EVEN NUMBERS
# number=list(map(int,input('enter number: ').split()))
# even=list(filter(lambda x:x%2==0,number))
# print('even number is:',even)

    #7 WORDS LESS THAN 4 CHAR
# s=['hi','buddy','this','is','ss']
# filt=list(filter(lambda x:(len(x)<=4),s))
# print('words less than 4 char:',filt)

    #8 NUMBER GREATER THAN 10
# number=list(map(int,input('enter number: ').split()))
# filt=list(filter(lambda x:x>10,number))
# print('number greater than 10:',filt)

    #10 NUMBER NOT DIV BY 3
# number=list(map(int,input('enter number: ').split()))
# filt=list(filter(lambda x:x%3!=0,number))
# print('number not divisible by 3:',filt)

    #11 NEGATIVE NUMBER
# number=list(map(int,input('enter number: ').split()))
# filt=list(filter(lambda x:x<0,number))
# print('negative number:',filt)

    #13 PROD OF NUMBERS
# from functools import reduce
# number=list(map(int,input('enter number: ').split()))
# filt=reduce(lambda x, y: x*y,number)
# print('product of numbers is:',filt)

    #14 CONCAT STRING
# from functools import reduce
# s=['hi',' ','buddy!']
# con=reduce(lambda x,y:x+y,s)
# print('given string is:',con)

    #16 SUM OF SQUARES
# from functools import reduce
# number=[1,2,3]
# red=reduce(lambda x,y:(x+y)**2,number)
# print('sum of squares is:',red)

    #17 FACT OF NUM
# from functools import reduce
# n=int(input('enter number:'))
# numbers = range(1, n + 1)
# filtered_numbers = filter(lambda x: x > 0, numbers)
# mapped_numbers = map(lambda x: x, filtered_numbers)
# x=reduce(lambda x, y: x * y, mapped_numbers)
# print('factorial of number is:',x)


        #MODULES
# import math
# num = 25
# print(f"Square root of {num} is:", math.sqrt(num))
# n = 5
# print(f"Factorial of {n} is:", math.factorial(n))
# angle = 90
# radians = math.radians(angle)  
# print(f"Sin({angle}°) is:", math.sin(radians))

# import random
# rand_int = random.randint(1, 100)
# print("Random Integer:", rand_int)
# rand_float = random.random()
# print("Random Float:", rand_float)
# fruits = ["apple", "banana", "cherry", "grape"]
# random_fruit = random.choice(fruits)
# print("Random Fruit:", random_fruit)
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print("Shuffled Numbers:", numbers)
