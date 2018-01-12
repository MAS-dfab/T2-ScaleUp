import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Edge as Edge
from Constants import *

# class which extends the AbstractRule class
class Facade1(AbstractRule):

    def __init__(self):
        self.factorSubX = 2
        self.factorSubY = 6
        self.factorExtrude = 3 #to provide shading

    # method needs to be called replace and needs to take mesh as argument and
    # return a mesh
    def replace(self, oldMesh):
        newMesh = Mesh()
        # myEdge = Edge()
        myEdges = []
        for face in oldMesh.faces:
            edges = face.getEdges()
            myEdges.append(edges[1])
        for edge in myEdges:
            myFloors = int(edge.getLength()/3) # somethin is wrong with myFloors 3.0 meters is not fixed
                
        for face in oldMesh.faces:
        # if highRise:
            if face.group == typeFacade1:
                newFaces1 = FaceRules.splitGrid(face, myFloors, 1)
                for i,face in enumerate(newFaces1):
                    mid = range(myFloors/3,(myFloors/3)*2)
                    if i%2 == 0 and i != 0 and i not in mid:
                        newFaces2 = FaceRules.extrude(face, self.factorExtrude)
                        for aFace in newFaces2:
                            newMesh.addFace(aFace)  # storing new face into new mesh
                    else: #other group will get only this list
                        newFaces3 = FaceRules.splitGrid(face, self.factorSubX, self.factorSubY)
                        for aFace in newFaces3:
                            newMesh.addFace(aFace)
            else:
                newMesh.addFace(face)    
            # elif lowrise:
                
            #     for face in oldMesh.faces:
            #         newFaces4 = FaceRules.splitGrid(face, self.factorSubX, self.factorSubY)
            #         for aFace in newFaces4:
            #             newMesh.addFace(aFace)
                
                
        newMesh.constructTopology()
        return newMesh

# class which extends the AbstractFactoryRule class, used to fabricate the Rule
class FactoryFacade1(AbstractFactoryRule):

    def fabricateRule(self):
        facade1 = Facade1()
        facade1.factorSubX = int(self.slideFaceSubX.getValue())
        facade1.factorSubY = int(self.slideFaceSubY.getValue())
        facade1.factorExtrude = self.slideFaceExtrude.getValue()
        return facade1

    def addComponents(self, component):
        self.slideFaceSubX = self.engine.cp5.addSlider(component.getName() + "test")
        self.slideFaceSubX.setPosition(20, 40)
        self.slideFaceSubX.setRange(1, 3)
        self.slideFaceSubX.setLabel("Subdivision X")
        self.slideFaceSubX.moveTo(component)

        self.slideFaceSubY = self.engine.cp5.addSlider(component.getName() + "test2")
        self.slideFaceSubY.setPosition(20, 60)
        self.slideFaceSubY.setRange(2, 8)
        self.slideFaceSubY.setLabel("Subdivision Y")
        self.slideFaceSubY.moveTo(component)
        
        self.slideFaceExtrude = self.engine.cp5.addSlider(component.getName() + "test3")
        self.slideFaceExtrude.setPosition(20, 80)
        self.slideFaceExtrude.setRange(-4,4)
        self.slideFaceExtrude.setLabel("Extrude")
        self.slideFaceExtrude.moveTo(component)