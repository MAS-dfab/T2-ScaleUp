import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node

class RuleTaperedPY(AbstractRule):
    def __init__(self):
        self.extrude = 100
        self.close = True
        self.offset=0.3
        self.iterations=3
        self.rnd=0.3
    def replace(self,meshIn):
        newMesh = Mesh()
        for face in meshIn.faces:
            taperFace=face
            for j in range(self.iterations):
                normal = taperFace.getNormal()
                
                center = taperFace.getCenterAverage()
                normal.mult(self.extrude)
                rV=PVector(random(-self.extrude*self.rnd,self.extrude*self.rnd))
                normal.add(rV)
                normal.setMag(self.extrude)
                #center.add(normal)
               
                newNodes = []
                for node in taperFace.points:
                    dir = PVector.sub(center, node)
                    dir.mult(self.offset)
                    dir.add(node)
                    dir.add(normal)
                    newNodes.append(Node(dir))
                for i in range(taperFace.getNumPoints()):
                    n1 = taperFace.getPoint(i)
                    n2 = taperFace.getPoint((i + 1) % taperFace.getNumPoints())
                    n3 = newNodes[(i + 1) % taperFace.getNumPoints()]
                    n4 = newNodes[(i) % taperFace.getNumPoints()]
                    newFace = newMesh.addFace(n1, n2, n3, n4)
                    newFace.inheritPropertiesFrom(face)
                taperFace=Face(newNodes)
            if self.close:
                newFace = newMesh.addFace(taperFace)
                newFace.inheritPropertiesFrom(face)
        newMesh.constructTopology()
        return newMesh

class FactoryRuleTaperedPY(AbstractFactoryRule):
    def fabricateRule(self):
        rule=RuleTaperedPY()
        rule.extrude=self.sliderExtrude.getValue()
        rule.rnd=self.sliderRnd.getValue()
        rule.iterations=int(self.sliderIterations.getValue())
        rule.offset=self.sliderOffset.getValue()
        rule.close=self.toggleClose.getBooleanValue()
        return rule
    def addComponents(self,component):
        self.sliderExtrude=self.engine.cp5.addSlider(component.getName()+"extrude")
        self.sliderExtrude.setPosition(20,40)
        self.sliderExtrude.setRange(-100,100)
        self.sliderExtrude.setLabel("extrude")
        self.sliderExtrude.moveTo(component)
        
        self.sliderRnd=self.engine.cp5.addSlider(component.getName()+"random")
        self.sliderRnd.setPosition(20,60)
        self.sliderRnd.setRange(0,1)
        self.sliderRnd.setLabel("random")
        self.sliderRnd.moveTo(component)
        
        self.sliderIterations=self.engine.cp5.addSlider(component.getName()+"iterations")
        self.sliderIterations.setPosition(20,80)
        self.sliderIterations.setRange(1,10)
        self.sliderIterations.setLabel("iterations")
        self.sliderIterations.moveTo(component)
        self.sliderIterations.setNumberOfTickMarks(10)
        
        self.sliderOffset=self.engine.cp5.addSlider(component.getName()+"offset")
        self.sliderOffset.setPosition(20,100)
        self.sliderOffset.setRange(-1,1)
        self.sliderOffset.setLabel("offset")
        self.sliderOffset.moveTo(component)
        
        self.toggleClose=self.engine.cp5.addToggle(component.getName()+"close")
        self.toggleClose.setPosition(20,120)
        self.toggleClose.setLabel("close")
        self.toggleClose.moveTo(component)