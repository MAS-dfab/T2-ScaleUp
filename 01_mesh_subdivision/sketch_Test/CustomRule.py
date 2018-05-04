import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face

# class which extends the AbstractRule class
class RulePyramid(AbstractRule):
    def __init__(self):
        self.factorExtrude = 100
        self.factorExtrude2 = 100
    
    #method for subdivision, has to be named replace
    def replace(self, mesh):
        newMesh=Mesh()
        for face in mesh.faces:
            extrusion = self.factorExtrude
            if random(1) > 0.5:
                extrusion = self.factorExtrude2
            newFaces=FaceRules.extrudeToPoint(face, extrusion)
            for cFace in newFaces:
                newMesh.addFace(cFace)
        newMesh.constructTopology()
        return newMesh
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryRulePyramid(AbstractFactoryRule):
    def fabricateRule(self):
        rulePyramid=RulePyramid()
        rulePyramid.factorExtrude=self.slideFaceMove.getValue()
        rulePyramid.factorExtrude2=self.slideFaceMove2.getValue()
        return rulePyramid
    
    #add slider to the GUI, has to be named addComponents
    def addComponents(self,component):
        self.slideFaceMove=self.engine.cp5.addSlider(component.getName()+"test")
        self.slideFaceMove.setPosition(20,20)
        self.slideFaceMove.setRange(-100,100)
        self.slideFaceMove.setLabel("moveMe")
        self.slideFaceMove.moveTo(component)
        
        self.slideFaceMove2=self.engine.cp5.addSlider(component.getName()+"test2")
        self.slideFaceMove2.setPosition(20,60)
        self.slideFaceMove2.setRange(-100,100)
        self.slideFaceMove2.setLabel("moveMe2")
        self.slideFaceMove2.moveTo(component)