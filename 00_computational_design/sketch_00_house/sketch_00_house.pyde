from Classes import Rectangle

def setup():
    size(1600,900)
    
def draw():
    background(0)
    
    r1 = Rectangle(10,10,800,600)
    rect(r1.x1,r1.y1,r1.x2,r1.y2)
    
    r2 = Rectangle(400,100,500,500)
    rect(r2.x1,r2.y1,r2.x2,r2.y2)
