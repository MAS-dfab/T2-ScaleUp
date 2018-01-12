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

class Grid3D:
     #for x in range(grid.nX-1):
        #for y in range(grid.nY-1):
           # for y in range(grid.nY-1):
    def __init__(self,nX,nY,nZ):
        self.nX=nX
        self.nY=nY
        self.nZ=nZ
        self.nYZ=self.nY*self.nZ
    def getIndex(self,x,y,z):
        return x * self.nYZ + y*self.nZ + z
    def getX(self,index):
        return index / self.nYZ
    def getY(self,index):
        return (index / self.nZ) % self.nY
    def getZ(self,index):
        return index % self.nZ
    
        