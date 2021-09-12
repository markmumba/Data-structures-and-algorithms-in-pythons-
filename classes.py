class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    def know_age_10yrs(self):
        return self.age + 10
    
    
Puppy = Dog('Simba',10)
print(Puppy.know_age_10yrs())
print(Puppy.name)

    