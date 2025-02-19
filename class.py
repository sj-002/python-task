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
class library:
    def __init__(self,fiction_row,history_row,mystery_row,nonfiction_row):
        self.fiction_row=fiction_row
        self.history_row=history_row
        self.mystery_row=mystery_row
        self.nonfiction_row=nonfiction_row
        
    def fiction(self):
        print(f'Fiction books are in the {self.fiction_row}')
    def history(self):
        print(f'History books are in the {self.history_row}')
    def mystery(self):
        print(f'Mystery books are in the {self.mystery_row}')
    def nonfiction(self):
        print(f'Non-fiction books are in the {self.nonfiction_row}')

lib=library('row 1','row 2', 'row 3', 'row 4')
lib.fiction()
lib.history()
lib.mystery()
lib.nonfiction()

lib2=library('row 4 for lib2', 'row 1 for lib2','row 2 for lib2','row 3 for lib2')
lib2.history()
lib2.mystery()
lib2.nonfiction()
lib2.fiction()


    