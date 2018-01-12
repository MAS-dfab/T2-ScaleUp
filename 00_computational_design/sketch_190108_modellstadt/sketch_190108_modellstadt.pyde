# json file format, based on javascript, similar to xml, store hierarchical data
add_library('jsonsimple')
add_library('peasycam')
add_library('controlP5')
# hdgeom used for geometric definitions
add_library('hdgeom')


from CustomRule import FactoryRuleStreet
from Urban import FactoryUrbanPlanning
from LowriseClass import FactoryLowrise
from Highrise_2 import FactoryHighRise
from Facade1 import FactoryFacade1
from facadeRule import FactoryRuleBalcony
from roof import FactoryRulePyramid
from OpenSpaceClass import FactoryOpenSpace

from CustomAnalyse import AnalyseGroup
from GroupRenderer import GroupRenderer

def setup():
    # global variable 'engine'
    global engine, f
    size(1600,900,P3D)
    # create a class called SubdivisionEngine
    engine = SubdivisionEngine(this,sketchPath())
    engine.registerRule("Street Rule",FactoryRuleStreet())
    engine.registerRule("Urban Planning",FactoryUrbanPlanning())
    engine.registerRule("Lowrise",FactoryLowrise())
    engine.registerRule("Highrise",FactoryHighRise())
    engine.registerRule("Facade1",FactoryFacade1())
    engine.registerRule("Facade2",FactoryRuleBalcony())
    engine.registerRule("Roof",FactoryRulePyramid())
    engine.registerRule("Open Space",FactoryOpenSpace())
    
    engine.registerAnalyserFace("Area", AnalyseFaceArea())
    engine.registerAnalyserFace("Group", AnalyseGroup())
    engine.registerRenderer("Standard", Renderer());
    engine.registerRenderer("Group Render", GroupRenderer());
    # initialise the ui
    engine.initGui()
    #initialise the first mesh
    f = Face(-150, 250, 150, -250)
    m = Mesh()
    m.addFace(f)
    engine.initMesh(m)
    

    
def draw():
    global engine, f
    
    # call the methods
    engine.draw()
    engine.drawGUI()






    