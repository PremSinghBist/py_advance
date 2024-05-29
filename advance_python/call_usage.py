class Call_usage:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self) :
        print(f" Sum is ",self.a + self.b)
    
    def __call__(self):
        print("Call method is invoked")

c = Call_usage(5, 3)
c.sum()
c()  #Call method is invoked when you invoke the class without parameter 