import hdgeom.mesh.analyse.AnalyseFace as AnalyseFace
import hdgeom.mesh.Face as Face

#simple class which analyses the group of a face
class AnalyseGroup(AnalyseFace):
    def getFaceValue(self,face):
        return face.group