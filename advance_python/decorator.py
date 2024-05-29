#Decorator wrap the function with addtional functionality
def my_decorator(function):
    def wrapper():
        function()
        print("Hi am decorating your function")
    
    return wrapper()

def hello_world():
    print("Hello World")
    
my_decorator(hello_world)