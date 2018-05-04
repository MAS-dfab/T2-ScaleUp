add_library('quickhull3D')
add_library('peasycam')
add_library('jsonsimple')
add_library('hdgeom')
add_library('controlP5')

def setup():
    global face
    global faces
    size(1600,900,P3D)
    cam=PeasyCam(this,200)
    face=Face()
    face.addPoint(-50,-100,0)
    face.addPoint(50,-100,0)
    face.addPoint(50,100,0)
    face.addPoint(-50,100,0)
    faces=splitRel(face,0,[0.20,0.80])
    newFaces=[]
    for f in faces:
        newFaces.extend(splitRel(f,1,[0.1,0.5,0.9]))
    faces=newFaces
    # warning: new vertices will not be welded.
    
def draw():
    background(0)
    lights()
    # face.display3D(g)
    for f in faces:
        f.display3D(g)

def getPointBetweenRel( v1,  v2,  f):
    return  PVector((v2.x - v1.x) * f + v1.x, (v2.y - v1.y) * f + v1.y, (v2.z - v1.z) * f + v1.z)

def splitRel(f,dir,splits):
    nSplits=len(splits)
    sA = [None]*(nSplits + 2)# create list of split nodes for edge 
    sA[0] = f.getPoint(dir)# add start node
    sA[nSplits + 1] = f.getPoint(dir + 1)# add end node

    sB = [None]*(nSplits + 2)# create list of split nodes for opposite edge
    sB[0] = f.getPoint((dir + 3)) # add start node
    sB[nSplits + 1] = f.getPoint((dir + 2) % f.getNumPoints())# add end node

    for i in  range(nSplits):
        sA[i + 1] = getPointBetweenRel(sA[0], sA[nSplits + 1], splits[i])
        sB[i + 1] = getPointBetweenRel(sB[0], sB[nSplits + 1], splits[i])
    
    result = [None]*(nSplits + 1)# list for all new faces
    for i in  range(nSplits+1) :
      if dir == 1:
        result[i] = Face(sB[i], sA[i], sA[i + 1], sB[i + 1])
      else:
        result[i] = Face(sB[i], sB[i + 1], sA[i + 1], sA[i])
    return result
  