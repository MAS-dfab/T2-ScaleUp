add_library('peasycam')
add_library('jsonsimple')
add_library('hdgeom')
add_library('controlP5')

import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Node as Node
import hdgeom.mesh.Edge as Edge
import hdgeom.mesh.Face as Face
import hdgeom.mesh.functions.MeshFacesFromLines as MeshFacesFromLines

def setup():
    global mesh
    size(1600,900,P3D)
    
    cam = PeasyCam(this,300)
    # load lines and create a mesh with faces from the line network. the tolerance defines maxmimum distances of vertices to be fused 
    mesh=MeshFacesFromLines.meshFromLines(sketchPath("")+"/polylines.csv",0.01)
    mesh.constructTopology();

def draw():
    background(0)
    scale(5);
    strokeWeight(0.2)
    randomSeed(1)
    for f in mesh.faces:
        fill(random(255),random(255),random(255))
        f.display3D(g)
   
    
    