add_library('quickhull3D')
add_library('peasycam')
add_library('jsonsimple')
add_library('hdgeom')
add_library('controlP5')

import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Node as Node
import hdgeom.mesh.Edge as Edge
import hdgeom.mesh.Face as Face
import hdgeom.mesh.functions.MeshVertexWeld as MeshVertexWeld
import hdgeom.mesh.functions.MeshPiping as MeshPiping



def setup():
    global mesh
    size(1600,900,P3D)
    cam = PeasyCam(this,300)
    # load each group as separate mesh
    mesh=Mesh(sketchPath("")+"/mesh.obj")
    mesh.constructTopology()
    # mesh, number of segments, radius, radius node detail
    mesh=MeshPiping.pipe(mesh,5,3,7)

def draw():
    background(0)
    lights()
    scale(2)
    mesh.display3D(g)
    
    