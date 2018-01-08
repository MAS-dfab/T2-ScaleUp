import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face

# class which extends the AbstractRule class
class RulePyramid(AbstractRule):
    def __init__(self):
        self.factorExtrude=100
    def replace(self, mesh):
        newMesh=Mesh()
        for face in mesh.faces:
            newFaces=FaceRules.extrudeToPoint(face, self.factorExtrude)
            counter=0
            for cFace in newFaces:
                cFace.group=counter
                newMesh.addFace(cFace)
                counter+=1
        newMesh.constructTopology()
        return newMesh
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryRulePyramid(AbstractFactoryRule):
    def fabricateRule(self):
        rulePyramid=RulePyramid()
        rulePyramid.factorExtrude=self.slideFaceMove.getValue()
        return rulePyramid
    def addComponents(self,component):
        self.slideFaceMove=self.engine.cp5.addSlider(component.getName()+"test")
        self.slideFaceMove.setPosition(20,20)
        self.slideFaceMove.setLabel("moveMe")
        self.slideFaceMove.moveTo(component)