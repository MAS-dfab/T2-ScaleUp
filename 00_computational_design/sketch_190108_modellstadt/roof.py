import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
from Constants import *

# class which extends the AbstractRule class
class RulePyramid(AbstractRule):
    def __init__(self):
        self.factorExtrude=100
        self.factorExtrude2=200
    
    def replace(self, mesh):
        newMesh=Mesh()
        for face in mesh.faces:
            if face.group == typeRoof:
                counter=0
                if face.getArea() > 300000:
                    newtFaces=FaceRules.splitGrid(face,20,30)
                    for t in newtFaces:
                        if random(1)>0.5:
                            faces = FaceRules.extrude(t,self.factorExtrude)
                            for f in faces:
                                newMesh.addFace(f)     
                        else:
                            newMesh.addFace(t)
                elif face.getArea() <= 300000 and face.getArea() > 200000:
                    newFaces=FaceRules.extrudeToPointTapered(face,self.factorExtrude,self.factorExtrude/3)
                    for cFace in newFaces:
                        cFace.group=counter
                        newMesh.addFace(cFace)
                elif face.getArea() <= 100000 and face.getArea() > 50000:
                    newFaces=FaceRules.extrudeToPoint(face,self.factorExtrude2)
                    for cFace in newFaces:
                        cFace.group=counter
                        newMesh.addFace(cFace)
                else :
                    newFaces=FaceRules.roof(face,self.factorExtrude)
                    for cFace in newFaces:
                        cFace.group=counter
                        newMesh.addFace(cFace)

            else:
                newMesh.addFace(face)
                
      
        newMesh.constructTopology()
        return newMesh
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryRulePyramid(AbstractFactoryRule):
    def fabricateRule(self):
        rulePyramid=RulePyramid()
        rulePyramid.factorExtrude=self.slideFaceMove.getValue()
        rulePyramid.factorExtrude2=self.slideFaceMove2.getValue()
        return rulePyramid
    def addComponents(self,component):
        self.slideFaceMove=self.engine.cp5.addSlider(component.getName()+"test")
        self.slideFaceMove.setPosition(20,20)
        self.slideFaceMove.setRange(0,10)
        self.slideFaceMove.setLabel("Larger")
        self.slideFaceMove.moveTo(component)
        
        self.slideFaceMove2=self.engine.cp5.addSlider(component.getName()+"Ruru")
        self.slideFaceMove2.setPosition(20,40)
        self.slideFaceMove2.setRange(0,10)
        self.slideFaceMove2.setLabel("Smaller")
        self.slideFaceMove2.moveTo(component)
        