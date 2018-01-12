import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node
from RuleSplit import RuleSplitPY
from Constants import *

# class which extends the RuleSplit class
class RuleCatmullPY(RuleSplitPY):
    def getNodePt(self,n):
        nbFaces = n.getFaces()
        sumFaces = PVector()
        for face in nbFaces:
            sumFaces.add(face.getCenterAverage())
        sumFaces.div(nbFaces.size())
        
        sumEdges = PVector()
        for edge in n.edges:
            sumEdges.add(edge.getCenter())
        sumEdges.mult(2.0 / n.getNumEdges())
        
        sumPos = PVector(n.x, n.y, n.z)
        sumPos.mult( n.getNumEdges() - 3)
        newPos = PVector()
        newPos.add(sumFaces)
        newPos.add(sumEdges)
        newPos.add(sumPos);
        newPos.div(n.getNumEdges())
        #normal = n.getNormal()
        #normal.mult(getNodeExtrude(n) * extrudeFactorNode)
        #newPos.add(normal);
        node = Node(newPos)
        node.comment=n.comment
        return node
    def getFacePt(self,face):
        node = Node(face.getCenterAverage())
    	#normal = face.getNormal()
    	#normal.mult(extrudeFactorFace);
    	#node.add(normal)
        return node
    def getEdgePt(self,edge):
        vSum = PVector()
        vSum.add(edge.n1)
        vSum.add(edge.n2)
        nFace = 0
        if (edge.f1 != None):
            nFace+=1
            vSum.add(edge.f1.getCenterAverage())
        if (edge.f2 != None):
            nFace+=1
            vSum.add(edge.f2.getCenterAverage())
        vSum.div(nFace + 2)
    	#normal = edge.getNormal()
    	#normal.mult(getEdgeExtrude(edge) * extrudeFactorEdge);
    	#vSum.add(normal)
        return  Node(vSum)

class FactoryRuleCatmullPY(AbstractFactoryRule):
    def fabricateRule(self):
        return RuleCatmullPY()