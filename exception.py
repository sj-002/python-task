    #1
# def reciprocal():
#     a=int(input('enter number:'))
#     try:
#         return 1 / a
#     except ZeroDivisionError:
#         return 'invalid operation'
# print(reciprocal()) 

    #2
# def reciprocal():
#     try:
#         a=int(input('enter number:'))
#         return 1/a
    # except ZeroDivisionError:
    #     return 'invalid operation'
    # except ValueError:
    #     return 'invalid value'
# print(reciprocal()) 

    #3
# def square():
#     try:
#         a=int(input('enter a:'))
#         print('square of a is:',a**2)
#     except ValueError:
#         print('invalid value')
#     else:
#         print('square operation performed successfully')
# square()

    #4
# def square():
#     try:
#         a=int(input('enter a:'))
#         print('square of a is:',a**2)
#     except ValueError:
#         print('invalid value')
#     else:
#         print('square operation performed successfully')
#     finally:
#         print('successfully printed')
# square()


def number():
    try:
       number=int(input('enter number:'))
       if number>0:
           print(number)
       else:
           pass
    except ValueError:
        print('input number is negative',)
number()


