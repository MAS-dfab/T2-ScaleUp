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
    def __init__(self):
        self.factorNode=0.0
        self.factorEdge=0.0
        self.factorFace=0.0
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
        normal = n.getNormal()
        normal.mult(self.factorNode)
        newPos.add(normal);
        node = Node(newPos)
        node.comment=n.comment
        return node
    def getFacePt(self,face):
        node = Node(face.getCenterAverage())
        normal = face.getNormal()
        normal.mult(self.factorFace);
        node.add(normal)
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
        normal = edge.getNormal()
        normal.mult(self.factorEdge);
        vSum.add(normal)
        return  Node(vSum)

class FactoryRuleCatmullPY(AbstractFactoryRule):
    def fabricateRule(self):
        rule= RuleCatmullPY()
        if self.toggleSmooth.getBooleanValue():
            rule.factorNode=0
            rule.factorFace=0
            rule.factorEdge=0
        else:
            rule.factorNode=self.sliderNode.getValue()
            rule.factorFace=self.sliderFace.getValue()
            rule.factorEdge=self.sliderEdge.getValue()
        return rule
    def addComponents(self,component):
        self.toggleSmooth=self.engine.cp5.addToggle(component.getName()+"smooth")
        self.toggleSmooth.setPosition(20,20)
        self.toggleSmooth.setLabel("smooth")
        self.toggleSmooth.moveTo(component)
        
        self.sliderNode=self.engine.cp5.addSlider(component.getName()+"node")
        self.sliderNode.setPosition(20,80)
        self.sliderNode.setRange(-100,100)
        self.sliderNode.setLabel("node factor")
        self.sliderNode.moveTo(component)
        
        self.sliderFace=self.engine.cp5.addSlider(component.getName()+"face")
        self.sliderFace.setPosition(20,100)
        self.sliderFace.setRange(-100,100)
        self.sliderFace.setLabel("face factor")
        self.sliderFace.moveTo(component)
        
        self.sliderEdge=self.engine.cp5.addSlider(component.getName()+"edge")
        self.sliderEdge.setPosition(20,120)
        self.sliderEdge.setRange(-100,100)
        self.sliderEdge.setLabel("edge factor")
        self.sliderEdge.moveTo(component)