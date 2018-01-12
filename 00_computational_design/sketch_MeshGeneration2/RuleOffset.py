import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node

class RuleOffsetPY(AbstractRule):
    def __init__(self):
        self.offset=10
        self.closeSides=True
    def replace(self,mesh):
        newMesh=Mesh()
        newNodes=[]
        for n in mesh.points:
            normal=n.getNormal()
            normal.setMag(self.offset)
            node = Node(n)
            node.add(normal)
            newNodes.append(node)
        for oldFace in mesh.faces:
            newFace= Face()
            for node in oldFace.points:
                newFace.addPoint(newNodes[node.id])
            newFace.inverse()
            newMesh.addFace(newFace)
            newMesh.addFace(oldFace)
        if self.closeSides==True:
            for face in mesh.faces:
                edges=face.getEdges()
                for e in edges:
                    if e.f1==None or e.f2==None:
                        newMesh.addFace(e.n2, e.n1, newNodes[e.n1.id], newNodes[e.n2.id])
        newMesh.constructTopology()
        return newMesh
        

  