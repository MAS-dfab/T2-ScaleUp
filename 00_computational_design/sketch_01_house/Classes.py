class Rectangle():
    def __init__(self, x1=0, y1=0, x2=100, y2=100):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def display(self, applet):
        applet.rect(self.x1,self.y1,self.x2,self.y2)
        
class House(Rectangle):
    def rise(self):
        self.y2 = self.y2+10