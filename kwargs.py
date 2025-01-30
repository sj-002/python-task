    #1 SUM 
# def args(*value):
#     x=sum(value)
#     print(x)
# args(1,2,3,4,5)

    #2 PROD
# def args(*value):
#     prod=1
#     for i in value:
#         prod*=i
#     print(prod)
# args(1,2,3,4,5) 

    #3 CONCATENATE ARGS
# def args(*value):
#     string=' '.join(value)     #join is a string method used to concatenate
#     print(string)
# args('this', 'is', 'my','mail')
    
    #3 ALITER
# def args(*value):
#     string=''
#     for values in value:
#         string = string+values
#     print(string)
# args('this','is','my','mail')    

    #4 ARGUMENTS AND KEYWORDS
# def x(day,year):
#     print('day is '+ day)
#     print('year is '+year)
# x(day='sunday',year='2025')

    #5 CONENT IN DICT
# def args(*thisdict):
#     dict ={
#     "fname": "suriya",
#     "lname": "shangar",
#     "mail": "ss@gmail"
#     }
#     print('content:',dict)
# args(dict)

            #LAMBDA
# def lam(a):
#     return lambda b: a+b
# result=lam(15)
# print('sum of a and b is:',result(10))

    #2 SQUARE OF NUM
# x=lambda a:a*a
# print(x(15))

    #1 RECURSION
# def recursion(k):
#     for i in range(k):
#         i=i+1
#         print(i)
# recursion(10)

    #2 SUM OF LIST
# def recursion(*k):
#     sum=0
#     for i in k:
#      sum=sum+i
#     print('sum is:',sum)
# recursion(2,4,6,8,10)



    #5 GET INPUT AND PRINT FACT
# import math
# def recursion(x):
#     if x<0:
#         print('invalid')
#     elif x==0:
#         print('factorial of zero is:',1)
#     else:
#         print('factorial of a number is:', math.factorial(x))
# number=(int(input('enter number:')))
# recursion(number)