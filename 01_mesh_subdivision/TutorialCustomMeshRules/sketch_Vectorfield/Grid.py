class GridList():
    def __init__(self,nX,nY):
        self.nX=nX
        self.nY=nY
        self.list=[None]*nX*nY
    def getIndex(self,x,y):
        return x*self.nY+y
    def getX(self,index):
        return index/self.nY
    def getY(self,index):
        return index%self.nY
    def set(self,x,y,value):
        self.list[self.getIndex(x,y)]=value
    def get(self,x,y):
        return self.list[self.getIndex(x,y)]
    def isInside(self,x,y):
        if x>=0 and x<self.nX and y>=0 and y<self.nY:
            return True
        return False

