    #1 Class and Obj
# class bank:
#     counter1="Loansection"
#     counter2="Depositsection"
#     counter3="Manager"

#     def loan(self):
#         print('loan section is counter 1')
#     def deposit(self):
#         print('deposit section is counter 2')
#     def manager(self):
#           print('manger section is counter 3')
# axis=bank()
# axis.loan()
# axis.deposit()
# axis.manager()

# sbi=bank()
# a=sbi.loan=('for loan counter 2')
# print(a)

        # EXAMPLE
# class Bank:
#     def __init__(self, loan_section, deposit_section, manager_section):
        # These are instance variables
        # self.loan_section = loan_section
        # self.deposit_section = deposit_section
        # self.manager_section = manager_section

    # def loan(self):
    #     print(f'Loan section is {self.loan_section}')

    # def deposit(self):
    #     print(f'Deposit section is {self.deposit_section}')

    # def manager(self):
    #     print(f'Manager section is {self.manager_section}')


# Creating an instance of Bank with custom values
# axis = Bank("Counter 1", "Counter 2", "Counter 3")
# axis.loan()      # Output: Loan section is Counter 1
# axis.deposit()   # Output: Deposit section is Counter 2
# axis.manager()   # Output: Manager section is Counter 3

# Creating another instance with different values
# sbi = Bank("Loan counter 1", "Deposit counter 2", "Manager counter 3")
# sbi.loan()       # Output: Loan section is Loan counter 1
# sbi.deposit()    # Output: Deposit section is Deposit counter 2
# sbi.manager()    # Output: Manager section is Manager counter 3

# Changing the value of the loan section for the 'sbi' object
# sbi.loan_section = 'New Loan Counter'
# sbi.loan()       # Output: Loan section is New Loan Counter


    #2 Class and obj using constructor
# class library:
#     def __init__(self,fiction_row,history_row,mystery_row,nonfiction_row):
#         self.fiction_row=fiction_row
#         self.history_row=history_row
#         self.mystery_row=mystery_row
#         self.nonfiction_row=nonfiction_row
        
#     def fiction(self):
#         print(f'Fiction books are in the {self.fiction_row}')
#     def history(self):
#         print(f'History books are in the {self.history_row}')
#     def mystery(self):
#         print(f'Mystery books are in the {self.mystery_row}')
#     def nonfiction(self):
#         print(f'Non-fiction books are in the {self.nonfiction_row}')

# lib=library('row 1','row 2', 'row 3', 'row 4')
# lib.fiction()
# lib.history()
# lib.mystery()
# lib.nonfiction()

# lib2=library('row 4 for lib2', 'row 1 for lib2','row 2 for lib2','row 3 for lib2')
# lib2.history()
# lib2.mystery()
# lib2.nonfiction()
# lib2.fiction()

        #INHERITANCE
    #1 SINGLE INHERITANCE
# class parent:
#     def bike(self):
#         print("dad's bike")
# class child(parent):
#     def car(self):
#         print("child's car")
# a=child()
# a.bike()
# a.car()

    #2 MULTIPLE INHERITANCE
# class parent:
#     def walk(self):
#         print('dad goes by walk')
# class son1:
#     def bike(self):
#         print('1st son rides a bike')
# class son2(son1,parent):
#     def car(self):
#         print('2nd son rides both bike and car')    
# a=son2()
# a.walk()
# a.bike()
# a.car()

    #3 MULTILEVEL INHERITANCE
# class parent:
#     def work(self):
#         print('dad is working')
# class son1(parent):
#     def school(self):
#         print('1st goes to school')
# class son2(son1):
#     def college(self):
#         print('elder son pursuing college')    
# a=son2()
# a.work()
# a.school()
# a.college()

    #4 HYBRID INHERITANCE
# class school:
#     def admin(self):
#         print('welcome to the school')
# class ground(school):
#     def prayer(self):
#         print('school time statrs by 8am')
# class canteen(school):
#     def interval(self):
#         print('mrng break time is 10:30')
# class administration(ground,canteen):
#     def office(self):
#         print('for enquiry contact office')
# a=administration()
# a.admin()
# a.prayer()
# a.interval()
# a.office()

    #5 HIERARCHICAL INHERITANCE
# class parent():
#     def read(self):
#         print('father has the habit of reading books')
# class son(parent):
#     def play(self):
#         print('son used to go the ground')
# class daughter(parent):
#     def yoga(self):
#         print('daughter used to do yoga daily')

# a=son()
# a.read()
# a.play()

# b=daughter()
# b.yoga()

    #6 OVERRIDING 
# class A:
#     def welcome(self):
#         print('hello')
# class B(A):
#     def welcome(self):
#         print('Hello buddy! Welcome')
# a=B()
# a.welcome()

    #7 SUPER KEYWORD
# class A:
#     def welcome(self):
#         print('Hey all')
# class B(A):
#     def welcome(self):
#         super().welcome()
#         print('Hello buddy! Welcome')
# a=B()
# a.welcome()


        #ENCAPSULATION
# class bank:
#     def __init__(self,username,id,pin):
#         self.username=username
#         self._id=id
#         self.__pin=pin

#     def name(self):
#         print(f'Account holder name: {self.username}')
#     def account_id(self):
#         print(f'Account id: {self._id}')
#     def account__pin(self):
#           print(f'User pin: {self.__pin}')
# a=bank('Suriya','91200002623','2902')
# a.name()
# a.account_id()
# a.account__pin()
