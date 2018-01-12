import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import random as rd
from Constants import *

# class which extends the AbstractRule class
# method needs to be called 'replace', needs to take a mesh as input
# and return a mesh as output

# class RulePyramid(AbstractRule):
#     def __init__(self):
#         self.factorExtrude=100
#     def replace(self, oldMesh):
#         newMesh=Mesh()
#         for face in oldMesh.faces:
#             newFaces=FaceRules.extrudeToPoint(face, self.factorExtrude)
#             counter=0
#             for cFace in newFaces:
#                 cFace.group=counter
#                 newMesh.addFace(cFace)
#                 counter+=1
#         newMesh.constructTopology()
#         return newMesh
    
# # class which extends the AbstractFactoryRule class, used to fabricate the Rule
# # method names have to be 'fabricateRule' and 'addComponents'
# class FactoryRulePyramid(AbstractFactoryRule):
#     def fabricateRule(self):
#         rulePyramid=RulePyramid()
#         rulePyramid.factorExtrude=self.slideFaceMove.getValue()
#         return rulePyramid
#     def addComponents(self,component):
#         self.slideFaceMove=self.engine.cp5.addSlider(component.getName()+"test")
#         self.slideFaceMove.setPosition(20,20)
#         self.slideFaceMove.setLabel("moveMe")
#         self.slideFaceMove.moveTo(component)
        
# moooooon

class HighRise(AbstractRule):
    def __init__(self):
        self.factorExtrude=100
        
    def replace(self, oldMesh):
        newMesh=Mesh()
        # oldMesh = random.sample(Face.Mesh,3)
        # sMesh = random.sample(Mesh, 3)

        for face in oldMesh.faces:
            if face.group == typePlotHighrise1:
                newFaces=FaceRules.splitOffset(face, 10)
                counter=0
                for i,cFace in enumerate(newFaces):
                    if i == 4:
                        cFace.group=typePlotEmpty2
                        newMesh.addFace(cFace)
                    else:        
                        i=rd.randrange(75, 150, 4)
                        newFaces=FaceRules.extrude(cFace, i)
                        for k,j in enumerate(newFaces):
                            if k == 4:
                                j.group = typeRoof
                            else:
                                if random(1) > 0.5:
                                    j.group = typeFacade1
                                else:
                                    j.group = typeFacade2
                            newMesh.addFace(j)
                        
                        

                    # for cFace in newFaces:
                    #     if counter==4:                
                    #         cFace.group=counter
                    #         newMesh.addFace(cFace)
                    #     else:
                    #         newSubFace=FaceRules.splitGrid(cFace,int(i/20),5)
                    #         for c in newSubFace:
                    #             newMesh.addFace(c)
                    counter+=1
            elif face.group == typePlotHighrise2:
                newFaces=FaceRules.splitOffset(face, -10)
                for i,cFace in enumerate(newFaces):
                    if i == 4:
                        cFace.group=typePlotEmpty2
                        newMesh.addFace(cFace)
                    else:        
                        i=rd.randrange(25, 50, 4)
                        newFaces=FaceRules.extrude(cFace, PVector(0,0,i))
                        for k,j in enumerate(newFaces):
                            if k == 4:
                                j.group = typeRoof
                            else:
                                if random(1) > 0.5:
                                    j.group = typeFacade1
                                else:
                                    j.group = typeFacade2
                            newMesh.addFace(j)
            else:
                newMesh.addFace(face)
        newMesh.constructTopology()
        return newMesh

class FactoryHighRise(AbstractFactoryRule):
    def fabricateRule(self):
        rulePyramid=HighRise()
        rulePyramid.factorExtrude=50
        return rulePyramid