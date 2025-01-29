        #area of sq
# def square():
#     print('area of square is:',a*a)
# a=5
# square()

        #area of rect
# def rect(l,b):
#     print('area of rectangle is:',l*b)
# rect(6,4)

        #even or odd
# def check(num):
#     if(num%2==0):
#         print('its a even number')
#     else:
#         print('its a odd number')
# num=int(input('enter number:'))
# check(num)

        #fact
# def fact(num):
#     fact=1
#     for i in range(1,num):
#         fact=fact*i
#     print(fact)
# num=int(input('enter num:'))
# fact(num)

# # Step 1: Define a function to check if a number is prime
# def is_prime(num):
#     # Step 2: Check if the number is less than 2
#     if num < 2:
#         return False  # Numbers less than 2 are not prime

#     # Step 3: Check if the number is divisible by 2 or 3
#     # if num == 2 or num == 3:
#     #     return True  # 2 and 3 are prime numbers

#     # Step 4: Check for divisibility from 2 to num-1
#     for i in range(2, num):
#         if num % i == 0:  # If num is divisible by i, it's not a prime number
#             return False  # Return False if we find a divisor

#     # Step 5: If no divisors were found, return True (it's a prime number)
#     return True

# # Step 6: Get user input for the number
# num = int(input("Enter a number: "))

# # Step 7: Display the result
        #PRIME NUMBER
# def prime(num):
#     if num<2:
#         return False
#     if num==2 and num==3:
#         return True
#     for i in range(2,num):
#         if(num%i==0):
#             return False
#     return True
# num=int(input('Enter number:'))
# if prime(num):
#     print(num,'is a prime number')
# else:
#     print(num,'not a prime number')

# Function to check if a number is prime
# def is_prime(number):
#     if number <= 1:  # Numbers less than or equal to 1 are not prime
#         return False
#     for i in range(2, int(number**0.5) + 1):  # Check for factors up to the square root of the number
#         if number % i == 0:  # If divisible, it's not prime
#             return False
#     return True  # If no factors found, it's prime

# # Input from the user
# num = int(input("Enter a number: "))

# # Check if the number is prime and print the result
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

        #sum of squares

        #COUNT CHRACTERS
# def character():
#     char=input('enter character:')
#     count=0
#     for x in char:
#         count=count+1
#     print('number of characters is',count)
# character()


        #SUM OF SQUARES
# def operation(num):
#     sum=0
#     for i in range(num):
#         sum=sum+i
#     print('sum is:',sum)
#     print('sq is:',sum*sum)
# num=int(input('enter number:'))
# operation(num)

#     print('sum of numbers is:',sum)
#     print('square of the sum is:',sum*sum)
# num=int(input('enter number:'))
# operation(num)


        #ARMSTRONG NUMBER
# num = int(input('Enter number: '))
# power = len(str(num))  # Number of digits in the number
# sum_of_powers = 0

# for i in str(num):
#     sum_of_powers += int(i) ** power

# if sum_of_powers == num:
#     print('Yes, it is an Armstrong number')
# else:
#     print('No, it is not an Armstrong number')

        #ALITER
# num=int(input('enter number:'))
# sum=0
# for x in str(num):
#     sum += int(x)**3
# if sum==num:
#     print(num,'is a Armstrong number')
# else:
#     print(num, 'is Not a armstrong number')

        #LEAP YEAR
# def year():
#      x=int(input('enter year:'))
#      if (x%4==0 and x%100!=0):
#         print('leap year')
#      else:
#         print('not a leap year')
# year()

# x=[1,2,3,1,4,2]
# seen=set()
# duplicate=[]
# for items in x:
#     if items in seen:
#         duplicate.append(items)
#     else:
#         seen.add(items)
# print('seen elements are:',seen)
# print('duplicate elements are:',duplicate)


    
