import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
from random import randint
from Constants import *
import hdgeom.primitives as primitives

# class which extends the AbstractRule class
class OpenSpace(AbstractRule):
    def __init__(self):
        self.h = 6

    #method for subdivision, has to be named replace
    def replace(self, mesh):
        newMeshes = []
        newMesh = Mesh()
        newMesh2 = Mesh()
        for face in mesh.faces:
            if face.group == typePlotEmpty:
                self.h = random(4,7)
                offsetX = random(-3,3)
                offsetY = random(-3,3)
                center = face.getCenterAverage()
                sphereHD = primitives.Sphere(center.x + offsetX,center.y + offsetY,self.h,self.h/2)
                sph = sphereHD.getMesh()
                boxHD = primitives.Box(center.x + offsetX-self.h/24,center.y + offsetY-self.h/24,0,center.x + offsetX +self.h/24,center.y + offsetY+self.h/24,self.h)
                bx = boxHD.getMesh()
                for tree in sph.faces:
                    newMesh.addFace(tree)
                for trunk in bx.faces:
                    newMesh2.addFace(trunk)
                newMeshes.append(newMesh)
                newMeshes.append(newMesh2)
                newMesh = Mesh()
                newMesh2 = Mesh()
                if face.getArea() > 70:
                    inner = FaceRules.splitOffset(face,4)
                    center = face.getCenterAverage()
                    for node in inner[4].points:
                        sphereHD = primitives.Sphere(node.x,node.y,self.h,self.h/2)
                        sph = sphereHD.getMesh()
                        boxHD = primitives.Box(node.x-self.h/24,node.y-self.h/24,0,node.x+self.h/24,node.y+self.h/24,self.h)
                        bx = boxHD.getMesh()
                        for tree in sph.faces:
                            newMesh.addFace(tree)
                        for trunk in bx.faces:
                            newMesh2.addFace(trunk)
                        newMeshes.append(newMesh)
                        newMeshes.append(newMesh2)
                        newMesh = Mesh()
                        newMesh2 = Mesh()
        for meshT in newMeshes:
            mesh.addMeshFacesNodes(meshT)
        return mesh
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryOpenSpace(AbstractFactoryRule):
    def fabricateRule(self):
        ruleOpenSpace=OpenSpace()
        return ruleOpenSpace
    
    #add slider to the GUI, has to be named addComponents
    def addComponents(self,component):
        pass