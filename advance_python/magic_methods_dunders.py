#Dunder --> __
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def __del__(self):
        #Automatically deletes the object 
        print("Object is being deconstructed")
        
    
        

p = Person("Mike", 24) 
#manuall deleting | del p
        