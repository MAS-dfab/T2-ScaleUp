add_library('jsonsimple')
add_library('peasycam')
add_library('controlP5')
add_library('hdgeom')

from CustomRule import FactoryRulePyramid
from RuleCatmull import FactoryRuleCatmullPY
from RuleSplit import FactoryRuleSplitPY
from RuleTranslatePY import FactoryRuleTranslatePY
from Analyser import AnalyseZValue
from Analyser import AnalyseDistance

from GroupRenderer import RendererGroup


def setup():
    global engine
    size(1600,900,P3D)
    engine = SubdivisionEngine(this,sketchPath(""))
    engine.registerRule("Pyramid Rule",FactoryRulePyramid())
    engine.registerRule("Rule Catmull",FactoryRuleCatmullPY())
    engine.registerRule("Rule Split",FactoryRuleSplitPY())
    engine.registerRule("Rule Translate",FactoryRuleTranslatePY())
    engine.registerPresets()
    engine.registerAnalyserFace("Analyse Z Value",AnalyseZValue())
    engine.registerAnalyserFace("Analyse Distance",AnalyseDistance())
    #engine.registerAnalyserFace("Area", AnalyseFaceArea())
    engine.registerRenderer("Standard", Renderer());
    engine.registerRenderer("Group", RendererGroup());
    engine.initGui()
    engine.initMesh(None)
    
def draw():
    global engine
    engine.draw()
    engine.drawGUI()





    