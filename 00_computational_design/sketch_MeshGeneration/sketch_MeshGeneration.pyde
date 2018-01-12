add_library('jsonsimple')
add_library('controlP5')
add_library('peasycam')
add_library('hdgeom')
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node
from Grid import Grid
def setup():
    size(900,600,P3D)
    cam=PeasyCam(this,300)
    global mesh,grid
    
    grid=Grid(50,100)
    
    mesh=Mesh()
    for x in range(grid.nX):
        for y in range(grid.nY):
            node=Node(x*10-(grid.nX*10.0/2),y*10-(grid.nY*10.0/2),10*sin(x*0.2)+20*sin(y*0.1))
            mesh.addNode(node)
            
    for x in range(grid.nX-1):
        for y in range(grid.nY-1):
            i1=grid.getIndex(x,y)
            i2=grid.getIndex(x+1,y)
            i3=grid.getIndex(x+1,y+1)
            i4=grid.getIndex(x,y+1)
            mesh.addFace(i1,i2,i3,i4)

def draw():
    background(0,0,255)
    lights()
    mesh.display3D(g)


    
    
    


    
