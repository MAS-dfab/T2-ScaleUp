class Grid():
    def __init__(self,nX,nY):
        self.nX=nX
        self.nY=nY
    def getIndex(self,x,y):
        return x*self.nY+y
    def getX(self,index):
        return index/self.nY
    def getY(self,index):
        return index%self.nY
    
        