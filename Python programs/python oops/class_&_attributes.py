

class Circle():

    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius
    
    def get_circumference(self):
        return 2*Circle.pi*self.radius #or you can write return 2*self.radius*self.pi
    
c=Circle()
perimeter=c.get_circumference()
print(perimeter)

