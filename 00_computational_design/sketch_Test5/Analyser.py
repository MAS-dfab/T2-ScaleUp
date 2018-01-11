import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.analyse.AnalyseFace as AnalyseFace
import hdgeom.mesh.GraphMeshFace as GraphMeshFace
import hdgeom.graph.Dijkstra as Dijkstra
class AnalyseZValue(AnalyseFace):
    def analyseFaceValues(self,mesh):
        faceValues=[0]*mesh.faces.size()
        for face in mesh.faces:
            faceValues[face.id]=face.getCenterAverage().z
        return faceValues
    
class AnalyseDistance(AnalyseFace):
    def analyseFaceValues(self,mesh):
        inputValues=[100000]*mesh.faces.size()
        for face in mesh.faces:
            edges=face.getEdges()
            for edge in edges:
                if edge.f1==None or edge.f2==None:
                    inputValues[face.id]=0 
            #if abs(face.getNormal().z)>0.99:
             #   inputValues[face.id]=0        
        graph=GraphMeshFace(mesh)#turn mesh into grap
        dijkstra=Dijkstra(graph,inputValues)# analyse the distance to faces 0 inside graph 
        return dijkstra.dist
                


