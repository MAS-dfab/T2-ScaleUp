add_library('jsonsimple')
add_library('controlP5')
add_library('peasycam')
add_library('hdgeom')
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node
import hdgeom.mesh.rules.RuleCatmull as RuleCatmull
from RuleOffset import RuleOffsetPY
from Grid import Grid3D
def setup():
    size(900,600,P3D)
    cam=PeasyCam(this,300)
    global mesh,grid
    grid=Grid3D(4,3,3)
    constructMesh()
    
def constructMesh(amplitude=0):
    global mesh
    mesh=Mesh()
    dim=30
    for x in range(grid.nX):
        for y in range(grid.nY):
            for z in range(grid.nZ):
                node=Node(x*dim-(grid.nX*dim/2),y*dim-(grid.nY*dim/2),z*dim+amplitude*sin(x))
                if x==0 or y==0 or x==grid.nX-1 or y==grid.nY-1:
                    node.fix=True
                    
                mesh.addNode(node)    
    for x in range(grid.nX-1):
        for y in range(grid.nY-1):
            for z in range(grid.nZ):
                i1=grid.getIndex(x,y,z)
                i2=grid.getIndex(x+1,y,z)
                i3=grid.getIndex(x+1,y+1,z)
                i4=grid.getIndex(x,y+1,z)
                if y==0 and x==1 and z==0:
                    i2=grid.getIndex(x+1,y,z+1)
                    i3=grid.getIndex(x+1,y+1,z+1)
                if z!=1 or x!=1 or y!=0:
                    mesh.addFace(i1,i2,i3,i4)
    mesh.constructTopology()
    rule=RuleCatmull()
    mesh=rule.replace(mesh)
    mesh=rule.replace(mesh)
    mesh=rule.replace(mesh)
    ruleOffset=RuleOffsetPY()
    ruleOffset.offset=2
    ruleOffset.closeSides=True
    mesh=ruleOffset.replace(mesh)
    
def draw():
    global mesh
    background(0,0,255)
    lights()
    
    noStroke()
    mesh.display3D(g)

def keyPressed():
    constructMesh(mouseX/3)
    print "keyPressed"
   
    
    
    


    