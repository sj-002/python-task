    #1 Using Args and Kwargs
# def function(add):
#     def operation(*args,**kwargs):
#         print('adding values')
#         result=add(*args,**kwargs)
#         print('success')
#         return result
#     return operation
        
# @function
# def greet(a,b):
#     print('sum is:',a+b)
#     # return a+b
# greet(5,5)

    #2 Using Function
# def function(msg):
#     def operation():
#         print('Welcome buddy!')
#         msg()
#         print('Glad to see you again')
#     return operation
  
# @function
# def greet():
#     print('Hope you are doing good')
# greet() 

    #3 Using Class
# class decorator:
#     def __init__(self,func):
#         self.func=func
#     def __call__(self,*args,**kwargs):
#         print('Welcome buddy!')
#         result=self.func(*args,**kwargs)
#         print('Glad to see you again')
#         return result
# @decorator
# def greet(name):
#     print(f"Hello,{name}") 
# greet('grece')   


        