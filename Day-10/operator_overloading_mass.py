#operator overloading in Python using the __add__ method
class mass:
    def __init__(self,kg=0,g=0):
        self.kg=kg+g//1000
        self.g=g%1000

    def __add__(self, other):
        total_kg=self.kg+other.kg
        total_g=self.g+other.g

        if(total_g>=1000):
            total_kg+=total_g//1000
            total_g=total_g%1000
            return mass(total_kg,total_g)
        
    def __repr__(self):
        return f'{self.kg}kg and {self.g}g'
    
mass1=mass(2,500)
mass2=mass(1,750)
mass3=mass1+mass2
print(mass3)