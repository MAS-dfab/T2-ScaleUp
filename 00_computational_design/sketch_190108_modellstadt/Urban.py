import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
from Constants import *

# class which extends the AbstractRule class

'''
class RuleMakeBlocks(AbstractRule):
    def __init__(self):
        self.nX = 3
        self.nY = 5
        
    def replace(self, mesh):
        newMesh=Mesh()
        
        for face in mesh.faces:
            
            newFaces=FaceRules.splitGrid(face, self.nX, self.nY)

            for cFace in newFaces:
                cFace.group=0 
                newMesh.addFace(cFace)

                 
        newMesh.constructTopology()
        return newMesh
    
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryMakeBlocks(AbstractFactoryRule):
    
    def fabricateRule(self):
        ruleMakeBlocks=RuleMakeBlocks()
        return ruleMakeBlocks
    
'''

class RuleUrbanPlanning(AbstractRule):
    def __init__(self):
        self.f1 = 18
        self.f2 = 5
        
    def replace(self, mesh):
        newMesh=Mesh()
        
        for face in mesh.faces:
            
            if face.group==typeBlock: #if is block then
                            
                indicator=random(1)
                
                #CREATE PARKS                
                if indicator<=0.1: #create simple empty plot
                    face.group = typePlotEmpty1 #Empty, park
                    newMesh.addFace(face)
                   
                    
                    
                #CREATE RESIDENTIAL AREAS
                elif 0.15 < indicator <=0.7: 
                    newFaces=FaceRules.splitGrid(face, 3, int(random(4, self.f2)))
                    
                    for f in newFaces:
                        r= random(1)
                        
                        if r<0.2:
                            f.group = typePlotEmpty1 #empty
                            
                        elif r > 0.9: #high
                            f.group = typePlotHighrise1
                            
                        else:
                            f.group = typePlotLowrise #low
                        
                        newMesh.addFace(f)
                
                    
                    
                    
                    
                #CREATE LANDMARKS            
                else: 
                    #newFaces=FaceRules.splitAbs(face, 0, random(5,self.f1))
                    newFaces=FaceRules.splitRel(face, 0, random(0.3,self.f1))
                
                    newFaces[0].group = typePlotEmpty2 #Empty, plaza
                    newFaces[1].group = typePlotHighrise2 #HighRize, Landmark


                    for cFace in newFaces:
                        newMesh.addFace(cFace)
            else:
                newMesh.addFace(face)
                 
                
                              
        newMesh.constructTopology()
        return newMesh
    
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryUrbanPlanning(AbstractFactoryRule):
    
    def fabricateRule(self):
        ruleUrbanPlanning=RuleUrbanPlanning()
        ruleUrbanPlanning.f1=self.slide1.getValue()
        ruleUrbanPlanning.f2=self.slide2.getValue()
        
        return ruleUrbanPlanning
    
    def addComponents(self,component):
        self.slide1=self.engine.cp5.addSlider(component.getName()+"landmarks")
        self.slide1.setPosition(20,20)
        self.slide1.setRange(0.15,0.75)
        self.slide1.setLabel("landmarks")
        self.slide1.moveTo(component)
        
        self.slide2=self.engine.cp5.addSlider(component.getName()+"residential")
        self.slide2.setPosition(20,80)
        self.slide2.setRange(6,10)
        self.slide2.setLabel("residential subdivision")
        self.slide2.moveTo(component) 
 