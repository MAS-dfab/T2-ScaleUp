import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
from Constants import *
from random import randint

# class which extends the AbstractRule class
class BalconyRules(AbstractRule):
    def __init__(self):
        self.factorExtrude=1
        #self.factorOffset=1 #not possible to use for the city
     
    def replace(self, mesh):
        newMesh=Mesh()
        for face in mesh.faces:
            if face.group == typeFacade2:        
                #newFaces=FaceRules.splitOffset(face,self.factorOffset)
                #counter=0
                #for i,sFace in enumerate(newFaces):
                    #sFace.group=counter
                    #newMesh.addFace(cFace)
                    
                    # if i==4:
                #offsetFaces = FaceRules.splitOffset(face,self.factorOffset)
                splitFaces = FaceRules.splitRel(face, 1 ,self.factorProportion)
                newsplitFaces=FaceRules.splitRel(splitFaces[1], randint(0,1) ,self.factorProportion)
                
                        #for snewFace in newsplitFaces:
                        
                            # newExList.addFace(snewFace(1))
                            
                            # for exFaces in newExList:
                            #    newExFaces = FaceRules.extrude(exFaces,30)
                            #newMesh.addFace(snewFace)
                newExFaces1 = FaceRules.extrude(newsplitFaces[1],self.factorExtrude1)
                newExFaces2 = FaceRules.extrude(newsplitFaces[0],self.factorExtrude) 
                
                newMesh.addFace(splitFaces[0])
                newExFaces1[4].group = typeFacade1
                newExFaces2[4].group = typeFacade1
                
                for exFace in newExFaces1:
                    newMesh.addFace(exFace)
                        
                for exFace in newExFaces2:
                    newMesh.addFace(exFace)
         
                    # else:
                    #newMesh.addFace(sFace)
                    #counter+=1
            else:
                newMesh.addFace(face)
                
        newMesh.constructTopology()
        return newMesh
    
    
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryRuleBalcony(AbstractFactoryRule):
    def fabricateRule(self):
        ruleBalcony=BalconyRules()
        #ruleBalcony.factorOffset=self.slideFaceMove.getValue()
        ruleBalcony.factorExtrude=self.slideFaceMove2.getValue()
        ruleBalcony.factorExtrude1=self.slideFaceMove3.getValue()
        ruleBalcony.factorProportion=self.slideFaceMove4.getValue()
        return ruleBalcony
    def addComponents(self,component):
        # self.slideFaceMove=self.engine.cp5.addSlider(component.getName()+"test")
        # self.slideFaceMove.setPosition(20,20)
        # self.slideFaceMove.setRange(0,1)
        # self.slideFaceMove.setLabel("Offset")
        # self.slideFaceMove.moveTo(component)
        
        self.slideFaceMove2=self.engine.cp5.addSlider(component.getName()+"test1")
        self.slideFaceMove2.setPosition(20,40)
        self.slideFaceMove2.setRange(-2,2)
        self.slideFaceMove2.setLabel("Balcony")
        self.slideFaceMove2.moveTo(component)
        
        self.slideFaceMove3=self.engine.cp5.addSlider(component.getName()+"test2")
        self.slideFaceMove3.setPosition(20,60)
        self.slideFaceMove3.setRange(-2,2)
        self.slideFaceMove3.setLabel("Balcony1")
        self.slideFaceMove3.moveTo(component)
        
        self.slideFaceMove4=self.engine.cp5.addSlider(component.getName()+"test3")
        self.slideFaceMove4.setPosition(20,80)
        self.slideFaceMove4.setRange(0,1)
        self.slideFaceMove4.setLabel("Proportion")
        self.slideFaceMove4.moveTo(component)