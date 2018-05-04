add_library('peasycam')
add_library('jsonsimple')
add_library('hdgeom')
add_library('controlP5')

import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Node as Node
import hdgeom.mesh.Edge as Edge
import hdgeom.mesh.Face as Face
import hdgeom.mesh.functions.MeshDual as MeshDual

def setup():
    global mesh,meshDualMesh
    size(1600,900,P3D)
    cam = PeasyCam(this,300)
    # load each group as separate mesh
    mesh=Mesh(sketchPath("")+"/mesh.obj")
    mesh.constructTopology();
    meshDualMesh=MeshDual.getDual(mesh);

def draw():
    background(0,0,255)
    scale(10)
    strokeWeight(0.1)
    stroke(0)
    fill(255)
    meshDualMesh.display3D(g)
    noFill()
    stroke(0,255,0)
    mesh.display3D(g)
    
    