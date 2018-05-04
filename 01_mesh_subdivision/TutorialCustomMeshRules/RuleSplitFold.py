import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node
from RuleSplit import RuleSplitPY

from Constants import *
class RuleSplitFoldPY(RuleSplitPY):
    def __init__(self):
        self.factorNode=0.0
        self.factorEdge=20.0
        self.factorFace=20.0

    def getFacePt(self,face):
        node=Node(face.getCenterAverage())
        normal=face.getNormal()
        normal.mult(self.factorFace)
        node.add(normal)
        return node
    def getEdgePt(self,edge):
        node =Node(edge.getCenter())
        dX=edge.n2.x-edge.n1.x
        dY=edge.n2.y-edge.n1.y
        dZ=edge.n2.z-edge.n1.z
        if dZ>dX and dZ >dY:
            normal=edge.getNormal()
            normal.mult(self.factorEdge)
            node.add(normal)
        return node
    
class FactoryRuleSplitFoldPY(AbstractFactoryRule):
    def fabricateRule(self):
        rule=RuleSplitFoldPY()
        return rule