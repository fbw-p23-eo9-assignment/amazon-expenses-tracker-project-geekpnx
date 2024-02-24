#--------------------------------
# Amazon expenses tracker project
#--------------------------------

#--------------------
# Home Greetings 
#--------------------

Banner = (
""" 
---------------------------------------------
|         AMAZON  EXPENSES TRACKER          |
---------------------------------------------
""")

Greetings = "      << Hello there, welcome! >>"

print(f'{Banner}\n   {Greetings}')
print()


#----------------
# Menu Options (1)
#----------------

lines= '-'*50
print(f'{lines}')

print()
print(f'1. Go to registration (if you are not yet a member)\n2. Go to login (if you already a member)')
print()

lst_option1 = []

x = input('Enter your option here (1/2): ')

# -------------------- Registration ------------

# un = input('Create Username: ')
# pw = input('Create Password: ')
# phn_nmbr = input('Phone number: ')

# print(f'{un}\n{pw}\n{phn_nmbr}')

def register(x):
   x = 'Your in registration'
   return x

print(register(x))
# def createUN():
#     return


# def createPW():
#     return

# def enterPhnNmb():
#     return

# -------------------- LOGIN ---------------------

def login():
    
    return



# def checkUN():
#     return


# def checkPW():
#     return


# -------------------- LOGIN ------------
