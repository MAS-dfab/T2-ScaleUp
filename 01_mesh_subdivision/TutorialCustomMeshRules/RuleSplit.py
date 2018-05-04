import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node
class RuleSplitPY(AbstractRule):
    def __init__(self):
        self.weights=[]
    def replace(self, oldMesh):
        # collectNodes
        faceNodes = [None]*oldMesh.faces.size()
        edgeNodes = [None]*oldMesh.edges.size()
        nodeNodes = [None]*oldMesh.points.size()
        for face in oldMesh.faces:
            faceNodes[face.id] = self.getFacePt(face)
        for edge in oldMesh.edges:
            edgeNodes[edge.id] = self.getEdgePt(edge)
        for node in oldMesh.points:
            nodeNodes[node.id] = self.getNodePt(node)
        # compose
        newMesh=Mesh()
        for face in oldMesh.faces:
            for ii in range(face.getNumPoints()):
              n1 = face.getPoint(ii)
              n2 = face.getPoint((ii + 1)%face.getNumPoints())
              n3 = face.getPoint((ii + 2)%face.getNumPoints())
              e1 = n1.getEdge(n2)
              e2 = n2.getEdge(n3)
              newNodes = [None]*4
              newNodes[0] = edgeNodes[e1.id]
              newNodes[1] = nodeNodes[n2.id]
              newNodes[2] = edgeNodes[e2.id]
              newNodes[3] = faceNodes[face.id]
              newFace = newMesh.addFace(newNodes)
              newFace.inheritPropertiesFrom(face)
        newMesh.constructTopology()
        return newMesh
    def getNodePt(self,oldNode):
        return Node(oldNode)
    def getFacePt(self,face):
        weightedCenter=PVector()
        totalWeight=0.0
                
        for i, node in enumerate(face.points):
            p=PVector(node.x,node.y,node.z)
            p.mult(self.weights[i])
            weightedCenter.add(p)
            totalWeight=self.weights[i]+totalWeight
        if totalWeight==0:
            totalWeight=1
        weightedCenter.div(totalWeight) 
        return Node(weightedCenter)
    def getEdgePt(self,edge):
        return Node(edge.getCenter())

class FactoryRuleSplitPY(AbstractFactoryRule):
    def fabricateRule(self):
        rule=RuleSplitPY()
        for slider in self.sliders:
            rule.weights.append(slider.getValue())
        return rule
    def addComponents(self,component):
        self.sliders=[]
        for i in range(4):
            slider=self.engine.cp5.addSlider(component.getName()+"weight"+str(i))
            slider.setPosition(20,20+i*20)
            slider.setRange(1,5)
            slider.setLabel("weight"+str(i))
            slider.moveTo(component)
            self.sliders.append(slider)
        