#lets have multiple excep blocks
#Getting alias for exception and print
try:
    a = int(input("Enter num 1 "))
    b = int(input( "Num 2"))
    c = a/b 
    #A is not defined here 
    d = a / z
    print("Division result ", c)
except ZeroDivisionError as divZError:
    print(f"Can't divide {a} by {b}", divZError)
except NameError as all_my_excepts:
    print("The other not handled exception printed here ", all_my_excepts)
else:
    print("Good You entered valid division numbers ")
    