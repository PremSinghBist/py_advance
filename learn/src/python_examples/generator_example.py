#Example to get fibonnaci number
#Get squre and print sum 
def fibo_num(nums):
    x, y = 0, 1
    for i in range(nums):
        x, y = y, x+y
        yield x
        
def square(nums):
    for num in nums:
        yield num**2
        
        
if __name__ == "__main__":
    print(sum(square(fibo_num(10))))