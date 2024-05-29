'''
    1. Decorator Definition:
    my_decorator_logger is a decorator function that accepts another function (function) as its argument.
    It creates a wrapper function (wrapper) that performs additional tasks before and after calling the original function.
    2. Wrapper Function:

    Retrieves the original function's name using function.__name__.
    Prints the function name to the console.
    Calls the original function with its arguments using function(*args, **kwargs).
    Opens a file named "myDecorator_logger.txt" in append mode ('+a').
    Writes a message to the file, including the function name and the returned value.
    Returns the result of the original function call.
    3. Function Decoration:

    The @my_decorator_logger syntax applies the decorator to the sum function.
    This effectively replaces the sum function with the wrapper function, so any calls to sum will now execute the wrapper's logic.
    4. Function Call:

    sum(20, 30) calls the decorated sum function (which is actually the wrapper).
    The following sequence of events occurs:
    The wrapper prints "Function name is: sum".
    The original sum function is called with a = 20 and b = 30.
    The original sum function calculates the sum and prints "Sum is 50".
    The wrapper writes a message to the file: "function name: sum, sum: 50".
    The wrapper returns the sum (50) as the final result.
    Key Points:

    Decorators provide a way to modify the behavior of functions without directly changing their code.
    They can be used for various purposes, such as logging, timing, caching, access control, and more.
    The *args and **kwargs syntax allows the wrapper to accept any number of arguments and pass them to the original function.
    This example demonstrates how decorators can be used to create a simple logging mechanism for functions.
'''
def my_decorator_logger(function):
 
    def wrapper(*args,  **kwargs):
        #Retrieve function name
        function_name = function.__name__
        print(f" Function name is : ", function_name)
        sum  = function(*args, **kwargs)
        with open("myDecorator_logger.txt", '+a') as file:
            msg = f"function name: {function_name}, sum : {sum} \n"
            file.write(msg)
        return sum 
    return wrapper


@my_decorator_logger        
def sum(a, b):
    sum = a + b 
    print("Sum is ", sum)
    return sum

sum(20, 30)