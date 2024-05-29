#Decorator wrap the function with addtional functionality
#https://www.youtube.com/watch?v=iZZtEJjQLjQ&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2
def my_decorator(function):
    def wrapper():
        function()
        print("Hi am decorating your function")
    
    return wrapper

#This is says that hello_world() function is decorated with my_decorator
#ie hello_world() gets executued from the my_decorator() only 
#ie hello_world() first goes to my_decorator and then from inside that it executes
@my_decorator
def hello_world():
    print("Hello World")

 
hello_world()