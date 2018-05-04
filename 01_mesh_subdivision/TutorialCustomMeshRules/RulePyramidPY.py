import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node
class RulePyramidPY(AbstractRule):
    def __init__(self):
        self.extrude=100
    def replace(self,meshIn):
        newMesh = Mesh()
        for face in meshIn.faces:
            normal = face.getNormal()
            normal.mult(self.extrude)
            center = face.getCenterAverage()
            center.add(normal)
            centerNode = Node(center)
            for  ii in range(face.getNumPoints()):
                n1 = face.getPoint(ii)
                n2 = face.getPoint((ii + 1) % face.getNumPoints())
                newFace = newMesh.addFace(n1, n2, centerNode)
                newFace.inheritPropertiesFrom(face)
        newMesh.constructTopology()
        return newMesh

class FactoryRulePyramidPY(AbstractFactoryRule):
    def fabricateRule(self):
        rule=RulePyramidPY()
        rule.extrude=self.sliderExtrude.getValue()
        return rule
    def addComponents(self,component):
        self.sliderExtrude=self.engine.cp5.addSlider(component.getName()+"extrude")
        self.sliderExtrude.setPosition(20,40)
        self.sliderExtrude.setRange(-100,100)
        self.sliderExtrude.setLabel("extrude")
        self.sliderExtrude.moveTo(component)