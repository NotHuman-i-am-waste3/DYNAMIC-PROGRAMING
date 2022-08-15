#creating an obj is an constructor for calling constructor use def __init__(self)

class S:
    def __init__(self,i,o):
        self.d=i
        self.b=o
        print(self.d,self.b)
        # if we not create self it will throw an error
    def display(self):
        print('within display method ',self.d,self.b)
# calling with parameters
a1=S(2,3)
a1.display()
# or
a1=S(8,9).display()