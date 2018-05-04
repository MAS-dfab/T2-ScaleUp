add_library('quickhull3D')
add_library('peasycam')
add_library('jsonsimple')
add_library('hdgeom')
add_library('controlP5')


def setup():
    global mesh
    size(1600,900,P3D)
    cam=PeasyCam(this,300)
    mesh=Mesh(sketchPath("")+"/mesh.obj")
    mesh=replace(mesh)
def replace(mesh):
    meshNew= Mesh()
    for face in mesh.faces:
        splitfaces=FaceRules.splitOffset(face,2)
        for splitface in splitfaces:
            meshNew.faces.add(splitface)
    return meshNew
def draw():
    background(0)
    lights()
    fill(255)
    mesh.display3D(g)
    
