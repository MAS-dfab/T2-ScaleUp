import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
from Constants import *

# class which extends the AbstractRule class
class RuleStreet(AbstractRule):
    def __init__(self):
        self.subdivFactor=2
        self.offsetDist=1  
         
    def replace(self, inputmesh):
        newMesh=Mesh()
        ## subdivide land ##
        for face in inputmesh.faces:
            sdf = int(self.subdivFactor)
            sdFaces=FaceRules.splitGrid(face, sdf, 2)
            ## subdivide street and lot ##
            for cFace in sdFaces:
                std = 0 - self.streetDist
                streetFaces=FaceRules.splitOffset(cFace, std)
                for i, stf in enumerate(streetFaces):
                    ## lot ##
                    if i == 4:
                        spd = self.splitDist
                        splitFaces = FaceRules.splitAbs(stf, 0, spd)
                        for i, spf in enumerate(splitFaces):
                            ## hedge ##
                            if i == 0:
                                hedgeFaces = FaceRules.extrude(spf, 1.2)
                                for hedge in hedgeFaces:
                                    newMesh.addFace(hedge)
                            else:
                                 swd = self.sidewalkDist
                                 lotFaces = FaceRules.splitOffset(spf, swd)
                                 for i, lf in enumerate(lotFaces):
                                     ## block ##
                                     if i == 4:
                                        lf.group = typeBlock
                                        newMesh.addFace(lf)
                                        #extrudeBlock = FaceRules.extrude(lf, 0)
                                        #for extrusion in extrudeBlock:
                                        #    newMesh.addFace(extrusion)
                                     ## sidewalk ##
                                     else:
                                        swFaces = FaceRules.extrude(lf, 0.2)
                                        for swf in swFaces:
                                            newMesh.addFace(swf)

                    ## street ##
                    else:
                        streetFaces = FaceRules.extrude(stf, 0)
                        for stf in streetFaces:
                            newMesh.addFace(stf)
   
                      
        newMesh.constructTopology()
        return newMesh
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryRuleStreet(AbstractFactoryRule):
    #fabricate the rule
    def fabricateRule(self):
        ruleStreet=RuleStreet()
        ruleStreet.subdivFactor=self.slideFaceMove.getValue()
        ruleStreet.sidewalkDist=self.slideFaceMove2.getValue()
        ruleStreet.streetDist=self.slideFaceMove3.getValue()
        ruleStreet.splitDist=self.slideFaceMove4.getValue()
        return ruleStreet
    def addComponents(self,component):
        self.slideFaceMove=self.engine.cp5.addSlider(component.getName()+"test1")
        self.slideFaceMove.setPosition(20,20)
        self.slideFaceMove.setRange(2,6)
        self.slideFaceMove.setNumberOfTickMarks(5)
        self.slideFaceMove.setLabel("SD FACTOR")
        self.slideFaceMove.moveTo(component)
        
        self.slideFaceMove2=self.engine.cp5.addSlider(component.getName()+"test2")
        self.slideFaceMove2.setPosition(20,60)
        self.slideFaceMove2.setRange(1.5,4)
        self.slideFaceMove2.setLabel("SIDEWALK WIDTH")
        self.slideFaceMove2.moveTo(component)
        
        self.slideFaceMove3=self.engine.cp5.addSlider(component.getName()+"test3")
        self.slideFaceMove3.setPosition(20,100)
        self.slideFaceMove3.setRange(3,6)
        self.slideFaceMove3.setNumberOfTickMarks(2)
        self.slideFaceMove3.setLabel("STREET WIDTH")
        self.slideFaceMove3.moveTo(component)
        
        self.slideFaceMove4=self.engine.cp5.addSlider(component.getName()+"test4")
        self.slideFaceMove4.setPosition(20,140)
        self.slideFaceMove4.setRange(0.6,1.2)
        self.slideFaceMove4.setNumberOfTickMarks(2)
        self.slideFaceMove4.setLabel("HEDGE WIDTH")
        self.slideFaceMove4.moveTo(component)