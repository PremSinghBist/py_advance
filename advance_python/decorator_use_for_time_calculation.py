import time
def time_decorator(function):
    def wrapper(*args, **kwargs):
        current_time = time.time() #current time in seconds
        function(*args, **kwargs)
        end_time = time.time()
        print("Total Execution time is taken  : ",end_time - current_time)
    return wrapper

@time_decorator
def sum(a, b):
    print ("The sum is : ", a + b)
    
sum(1000000005825558225885585585555, 1000000005825558225885585585555)
    
        
    