import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face
import hdgeom.mesh.Node as Node
from ParameterGroup import ParameterGroup
class RuleTranslatePY(AbstractRule):
    def replace(self,oldMesh):
        # clone the old mesh
        # oldMesh.getCopy()
        bounds=oldMesh.getBounds()
        newMesh=Mesh()
        newNodes=[None]*oldMesh.points.size()
        for node in oldMesh.points:
            newNodes[node.id]=Node(node)
        for face in oldMesh.faces:
            newFace=Face()
            newMesh.addFace(newFace)
            for node in face.points:
                newFace.points.add(newNodes[node.id])
        newMesh.constructTopology()
        # make a backup of the normals, not necessary if this is a copy of new mesh
        normalBackup=[None]*newMesh.points.size()
        for node in newMesh.points:
            normalBackup[node.id]=node.getNormal()
        # shift the nodes
        for node in newMesh.points:
            #nml=normalBackup[node.id]
            nml=oldMesh.getPoint(node.id).getNormal()
            translateMap=30*sin(map(node.y,bounds.y1,bounds.y2,0,30))
            nml.mult(translateMap)
            node.add(nml)
        return newMesh

class FactoryRuleTranslatePY(AbstractFactoryRule):
    def fabricateRule(self):
        return RuleTranslatePY()
    def addComponents(self,component):
        self.pg1=ParameterGroup(component.getName()+"parameters",self.engine)
        self.pg1.parameterGroup.moveTo(component)
