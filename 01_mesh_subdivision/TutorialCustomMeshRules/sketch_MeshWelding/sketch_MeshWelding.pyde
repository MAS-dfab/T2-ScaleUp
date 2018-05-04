add_library('peasycam')
add_library('jsonsimple')
add_library('hdgeom')
add_library('controlP5')

import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Node as Node
import hdgeom.mesh.Edge as Edge
import hdgeom.mesh.Face as Face
import hdgeom.mesh.functions.MeshVertexWeld as MeshVertexWeld

def setup():
    global mesh
    size(1600,900,P3D)
    cam = PeasyCam(this,300)
    # load each group as separate mesh
    mesh1=Mesh(sketchPath("")+"/group1.obj")
    for f in mesh1.faces:
        f.group=0
    mesh2=Mesh(sketchPath("")+"/group2.obj")
    for f in mesh2.faces:
        f.group=1
    # collect all faces in one mesh
    mesh=Mesh()
    mesh.faces.addAll(mesh1.faces)
    mesh.faces.addAll(mesh2.faces)
    # weld vertices closer then 0.1
    MeshVertexWeld.weldVertices(mesh,0.1) 
    mesh.constructTopology()
    

def draw():
    background(0)
    lights()
    strokeWeight(4)
    # draw borders
    for e in mesh.edges:
        if e.f1==None or e.f2==None:
            stroke(255,0,0)
        else:
            stroke(255)
        e.display3D(g)
    noStroke()
    # draw faces coloured by group
    for f in mesh.faces:
        if f.group==0:
            fill(0,255,0)
        elif f.group==1:
            fill(0,0,255)
        f.display3D(g)
    
    