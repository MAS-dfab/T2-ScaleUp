add_library('jsonsimple')
add_library('peasycam')
add_library('controlP5')
add_library('hdgeom')

from LowriseClass import FactoryLowrise
from OpenSpaceClass import FactoryOpenSpace
from CustomAnalyse import AnalyseGroup
from LowriseClass import Lowrise
from OpenSpaceClass import OpenSpace
import hdgeom.mesh.Mesh as Mesh
from Constants import *
import hdgeom.mesh.rules.FaceRules as FaceRules

def setup():
    global engine,mesh
    mesh = Mesh()
    faces = FaceRules.splitGrid(Face(0,0,150,80),5,7)
    for face in faces:
        if random(1) > 0.3:
            face.group = typePlotLowrise
        else:
            face.group = typePlotEmpty
        mesh.addFace(face)
    
    size(1600,900,P3D)
    engine = SubdivisionEngine(this,"/Users/alexanderenz/Desktop/Architektur/ETH/digitalMetal/test")
    engine.registerRule("Lowrise",FactoryLowrise())
    engine.registerRule("Open Space",FactoryOpenSpace())
    #engine.registerPresets()
    #engine.registerAnalyserFace("Area", AnalyseFaceArea())
    engine.registerAnalyserFace("Group", AnalyseGroup())
    engine.registerRenderer("Standard", Renderer());
    engine.initGui()
    engine.initMesh(mesh)
    
def draw():
    global engine
    engine.draw()
    engine.drawGUI()





    