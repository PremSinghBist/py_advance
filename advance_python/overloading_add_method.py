#How to acheive operator overloading_ | using dunder or special method
#Inside the __add__ method, you specified how the addition of two Vector objects should work
# In this case, you created a new Vector object whose x and y components are the sums of the corresponding components of the two original vectors.
'''
v1 + v2 
Traceback (most recent call last):
  File "/home/perm/example/advance_python/1.py", line 9, in <module>
    v3 = v1 + v2 
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
'''
class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def __add__(self, other):
        '''
        We are overloading the plus operator using __add__ dunder 
        '''
        return Vector(self.x + other.x, self.y + other.y)
    
    #how to get representation | or string representation
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    #overrides the lenght 
    def __len__(self):
        return 10
    
    def __call__(self):
        print(f"When the object is called what to do, this is the dunder method called")
        
v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2 
print(v3.x)
print(v3.y)
print(v3)
print("Lenght of vector ", len(v3))

    
        

        