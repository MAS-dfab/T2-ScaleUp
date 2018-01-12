add_library('jsonsimple')
add_library('peasycam')
add_library('controlP5')
add_library('hdgeom')

from CustomRule import FactoryRulePyramid
from RuleCatmull import FactoryRuleCatmullPY
from RuleSplit import FactoryRuleSplitPY
from RuleTranslatePY import FactoryRuleTranslatePY

from GroupRenderer import RendererGroup
from hdgeom.mesh import Mesh                                ###import mesh to intialize the Plane mesh 
from hdgeom.importexport.OBJImportExport import loadFromOBJ ###import Load from Obj

def setup():
    global engine
    size(1600,900,P3D)
    engine = SubdivisionEngine(this,sketchPath(""))
    engine.registerRule("Pyramid Rule",FactoryRulePyramid())
    engine.registerRule("Rule Catmull",FactoryRuleCatmullPY())
    engine.registerRule("Rule Split",FactoryRuleSplitPY())
    engine.registerRule("Rule Translate",FactoryRuleTranslatePY())
    engine.registerPresets()
    #engine.registerAnalyserFace("Area", AnalyseFaceArea())
    engine.registerRenderer("Standard", Renderer());
    engine.registerRenderer("Group", RendererGroup());
    inMesh=Mesh()
    #print sketchPath("")
    #print type(sketchPath)
    #print (sketchPath("")+"meshInput\plane.obj")
    
    inMesh=loadFromOBJ(sketchPath("")+"meshInput\PlaneObJ.obj")
    engine.initGui()
    engine.initMesh(inMesh)
    
def draw():
    global engine
    engine.draw()
    engine.drawGUI()





    