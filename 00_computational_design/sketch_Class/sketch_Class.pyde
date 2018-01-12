
def setup():
    size(600,600)
    global pt
    pt=Particle(1,1)
    
def draw():
    pt.move()
    pt.display()
       
class Point(object):
    def __init__(self,x=100,y=100,z=100):
        self.x=x
        self.y=y
        self.z=z
    def display(self):
        ellipse(self.x,self.y,30,30)
        
class Particle(Point):
    def __init__(self,stepX,stepY):
        Point.__init__(self)
        self.stepX=stepX
        self.stepY=stepY
    def move(self):
        self.x=self.x+self.stepX
        self.y=self.y+self.stepY
        if self.x>width:
            self.x=0
        if self.y>height:
            self.y=0
        
        
    