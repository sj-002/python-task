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


