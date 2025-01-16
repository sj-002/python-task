        #num from 1 to 10
# for i in range(1,11):
#     print(i)

        #sq of each number
# for i in range(1,11):
#     print(i*i)
     
        #char in str
# x='letter'
# for i in x:
#     print(i)

        #sum of numbers upto 10
# sum=0
# for i in range(1,11):
#     sum=sum+i
#     print(sum)

        #element in list
# x=['apple','boat','cat','dolphin','ex']
# for i in x:
#     print(i)

        #reverse order
# for i in range(10,0,-1):
#     print(i)

        #even num from 10 to 20
# for i in range(10,21):
#     if(i%2==0):
#         print(i)

        #mul of 5 b/t 20-50
# for i in range(20,51):
#     if(i%5==0):
#         print(i)

        #factorial
# fact=1
# for i in range(1,6):
#     fact = fact*i
#     print(fact)

        #num greater than 10
# x=[1,10,19,11,9]
# for i in x:
#     if(i>10):
#         print(i)

        #prime b/t 10 and 20
# for i in range(10,21):
#         if(i%2!=0 and i%3!=0):
#                 print(i)

        #largest num in list
# x=[2,1,5,4,3]
# largest_number=x[0]
# for num in x:
#         if num>largest_number:
#                 largest_number=num
# print('largest number is:',largest_number)

        #num of vowel in str
# str='letter'
# count=0
# for x in str:
#         if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
#                 print(x)
#                 count+=1
# print(count)

        #prod from 1 to 5
# prod=1 
# for i in range(1,6):
#         prod*=i
# print(prod)

        # print the product of numbers until user enter zero 
# prod=1
# while True:
#         number=int(input('Enter number:'))
#         if number==0:
#                 break
#         prod *= number
# print('product of the numbers is:',prod)       

#                 aliter

# prod = 1  # Initialize the product to 1
# first_input = True  # Flag to track if it's the first input

# while True:
#     number = int(input('Enter number: '))
    
#     if number == 0:  # If the user enters 0, exit the loop
#         if first_input:  # If it's the first input and the user entered 0
#             prod = 0  # Set product to 0 if no other number has been entered
#         break
    
#     prod *= number  # Multiply the product with the current number
#     first_input = False  # After the first valid input, set the flag to False

# print('Product of the numbers is:', prod)


        #  sum of numbers  until user enter negative number
# sum=0
# while True:
#         number=int(input('Enter number:'))
#         if number<0:
#                 break
#         sum += number
# print('sum of the numbers is:',sum)      