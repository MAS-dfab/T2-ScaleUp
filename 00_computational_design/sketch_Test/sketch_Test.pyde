add_library('jsonsimple')
add_library('peasycam')
add_library('controlP5')
add_library('hdgeom')

from CustomRule import FactoryRulePyramid
from CustomAnalyse import AnalyseGroup

def setup():
    global engine
    size(1600,900,P3D)
    engine = SubdivisionEngine(this,"/Users/dillenburger_b/Desktop/Test")
    engine.registerRule("Test Rule",FactoryRulePyramid())
    engine.registerAnalyserFace("Area", AnalyseFaceArea())
    engine.registerAnalyserFace("Group", AnalyseGroup())
    engine.registerRenderer("Standard", Renderer());
    engine.initGui()
    engine.initMesh(None)
    
def draw():
    global engine
    engine.draw()
    engine.drawGUI()





    