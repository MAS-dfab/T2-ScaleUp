import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
from random import randint
from Constants import *

# class which extends the AbstractRule class
class Lowrise(AbstractRule):
    def __init__(self):
        self.minExtrude = 3
        self.maxExtrude = 12
        self.minSplit = 0.4
        self.maxSplit = 0.6
        self.splits = 0.75
    
    #method for subdivision, has to be named replace
    def replace(self, mesh):
        newMesh=Mesh()
        for face in mesh.faces:
            if face.group == typePlotLowrise:
                if random(1) < self.splits:
                    extruded = FaceRules.extrude(face,randint(int(self.minExtrude/3),int(self.maxExtrude/3))*3)
                    splitted = FaceRules.splitRel(extruded[4],randint(0,1),random(self.minSplit,self.maxSplit))
                    extrudedSec = FaceRules.extrude(splitted[0],PVector(0,0,randint(0,2)*3))
                    extruded.remove(extruded[4])
                    splitted.remove(splitted[0])
                    for i,element in enumerate(extruded):
                        if i != 4:
                            if random(1) > 0.5:
                                element.group = typeFacade1
                            else:
                                element.group = typeFacade2
                    #splitted[0].group = typeTerrace
                    for i,element in enumerate(extrudedSec):
                        if i == 4:
                            element.group = typeRoof
                        elif random(1) > 0.5:
                            element.group = typeFacade1
                        else:
                            element.group = typeFacade2
                    newFaces = extruded
                    newFaces.extend(splitted)
                    newFaces.extend(extrudedSec)
                else:
                    extruded = FaceRules.extrude(face,randint(int(self.minExtrude/3),int(self.maxExtrude/3))*3)
                    for i,element in enumerate(extruded):
                        if i == 4:
                            element.group = typeRoof
                        elif random(1) > 0.5:
                            element.group = typeFacade1
                        else:
                            element.group = typeFacade2
                    newFaces = extruded
                for cFace in newFaces:
                    newMesh.addFace(cFace)
            else:
                newMesh.addFace(face)
            
        newMesh.constructTopology()
        return newMesh
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryLowrise(AbstractFactoryRule):
    def fabricateRule(self):
        ruleLowrise=Lowrise()
        ruleLowrise.minExtrude=self.minExtrude.getValue()
        ruleLowrise.maxExtrude=self.maxExtrude.getValue()
        ruleLowrise.minSplit=self.minSplit.getValue()
        ruleLowrise.maxSplit=self.maxSplit.getValue()
        ruleLowrise.splits=self.splits.getValue()
        return ruleLowrise
    
    #add slider to the GUI, has to be named addComponents
    def addComponents(self,component):
        self.minExtrude=self.engine.cp5.addSlider(component.getName()+"minExtrude")
        self.minExtrude.setPosition(10,20)
        self.minExtrude.setRange(3,18)
        self.minExtrude.setLabel("minExtrude")
        self.minExtrude.moveTo(component)
        
        self.maxExtrude=self.engine.cp5.addSlider(component.getName()+"maxExtrude")
        self.maxExtrude.setPosition(10,40)
        self.maxExtrude.setRange(3,18)
        self.maxExtrude.setLabel("maxExtrude")
        self.maxExtrude.moveTo(component)
        
        self.splits=self.engine.cp5.addSlider(component.getName()+"splits")
        self.splits.setPosition(10,60)
        self.splits.setRange(0,1)
        self.splits.setLabel("splits")
        self.splits.moveTo(component)
        
        self.minSplit=self.engine.cp5.addSlider(component.getName()+"minSplit")
        self.minSplit.setPosition(10,80)
        self.minSplit.setRange(0.2,0.8)
        self.minSplit.setLabel("minSplit")
        self.minSplit.moveTo(component)
        
        self.maxSplit=self.engine.cp5.addSlider(component.getName()+"maxSplit")
        self.maxSplit.setPosition(10,100)
        self.maxSplit.setRange(0.2,0.8)
        self.maxSplit.setLabel("maxSplit")
        self.maxSplit.moveTo(component)