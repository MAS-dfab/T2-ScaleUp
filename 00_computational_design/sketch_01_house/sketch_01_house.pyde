from Classes import Rectangle
from Classes import House

def setup():
    size(1600,900)
    rectMode(CORNERS)
    noFill()
    
def draw():    
    r1 = House(10,10,800,600)
    r1.display(this)
    
    r2 = House(400,100,950,500)
    r2.display(this)
