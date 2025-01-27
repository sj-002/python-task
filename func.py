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


# def character():
#     char=input('enter character:')
#     count=0
#     for x in char:
#         count=count+1
#     print('number of characters is',count)
# character()

# def operation(num):
#     sum=0
#     for i in range(num):
#         sum=sum+i
#     print('sum of numbers is:',sum)
#     print('square of the sum is:',sum*sum)
# num=int(input('enter number:'))
# operation(num)


