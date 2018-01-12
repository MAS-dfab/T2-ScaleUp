class ParameterGroup:
    def __init__(self,label,engine):
        self.engine=engine
        cp5= engine.cp5
        self.label=label
        self.parameterGroup = cp5.addGroup(self.label)
        self.parameterGroup.disableCollapse()
        self.parameterGroup.setWidth(200)
        self.parameterGroup.setBackgroundColor(20)
        self.parameterGroup.setBackgroundHeight(160)
        self.sliderConstant = cp5.addSlider(self.label + "Constant")
        self.radioFunction = cp5.addRadioButton(self.label + "FunctionRadio")
        self.radioFunction.setPosition(10, 0).setSize(10, 10)
        self.radioFunction.setColorForeground(color(120))
        self.radioFunction.setColorActive(color(255))
        self.radioFunction.setItemsPerRow(1)
        self.radioFunction.setSpacingColumn(10)
        self.radioFunction.setSpacingRow(5)
        self.radioFunction.addItem(self.label + "50", 0)
        self.radioFunction.addItem(self.label + "100", 1)
        self.radioFunction.addItem(self.label + "150", 2)
        self.radioFunction.addItem(self.label + "250", 3)
        self.radioFunction.getItem(0).setPosition(0, 10)
        self.radioFunction.getItem(1).setPosition(0, 30)
        self.radioFunction.getItem(2).setPosition(0, 60)
        self.radioFunction.getItem(3).setPosition(0, 90)
        self.radioFunction.hideLabels()
        self.radioFunction.getItem(0).toggle()
        self.radioFunction.setGroup(self.parameterGroup)
        self.sliderConstant = cp5.addSlider(self.label + "Constant")
        self.sliderConstant.setPosition(25, 10)
        self.sliderConstant.setGroup(self.parameterGroup)
        self.sliderConstant.setRange(-200, 200)
        self.sliderConstant.setCaptionLabel("Constant")
        self.listImage = cp5.addDropdownList(self.label + "Image")
        self.listImage.setPosition(25, 30)
        self.listImage.setGroup(self.parameterGroup)
        self.listImage.setLabel("Images")
        #self.listImage.setType(ScrollableList.DROPDOWN)
        self.listImage.setOpen(False)
        self.listImage.setColorBackground(color(0))
        self.listImage.setBackgroundColor(color(0))
        self.keyValues=[]
        for imageName in engine.imageMasks.keySet():
            self.keyValues.append(imageName)
        self.listImage.setItems(self.keyValues)

        self.rangeImage = cp5.addRange(self.label + "ImageRange")
        self.rangeImage.setPosition(25, 40)
        self.rangeImage.setGroup(self.parameterGroup)
        self.rangeImage.setRange(-100, 100)
        self.rangeImage.setCaptionLabel("Range")
        self.listHisto = engine.guiConstructHistogramList(self.label + "Histo")
        self.listHisto.setPosition(25, 60)
        self.listHisto.setGroup(self.parameterGroup)
        self.rangeHisto = cp5.addRange(self.label + "HistoRange")
        self.rangeHisto.setPosition(25, 70)
        self.rangeHisto.setGroup(self.parameterGroup)
        self.rangeHisto.setRange(-200, 200).setCaptionLabel("Range").setLowValue(0)
        self.listSino = engine.guiConstructHistogramList(self.label + "Sinus")
        self.listSino.setPosition(25, 90)
        self.listSino.setGroup(self.parameterGroup)
        self.sliderAmplitude = cp5.addSlider(self.label + "Amplitude")
        self.sliderAmplitude.setPosition(25, 100)
        self.sliderAmplitude.setGroup(self.parameterGroup)
        self.sliderAmplitude.setCaptionLabel("Amplitude")
        self.sliderAmplitude.setRange(0, 200)
        self.sliderFrequency = cp5.addSlider(self.label + "Frequency")
        self.sliderFrequency.setPosition(25, 110)
        self.sliderFrequency.setGroup(self.parameterGroup)
        self.sliderFrequency.setCaptionLabel("Frequency")
        self.sliderFrequency.setRange(0, 50)
        self.sliderPhase = cp5.addSlider(self.label + "Phase")
        self.sliderPhase.setPosition(25, 120)
        self.sliderPhase.setGroup(self.parameterGroup)
        self.sliderPhase.setCaptionLabel("Phase")
        self.sliderPhase.setRange(0, 4)
        self.sliderOffset = cp5.addSlider(self.label + "ruleOffset")
        self.sliderOffset.setPosition(25, 130)
        self.sliderOffset.setGroup(self.parameterGroup)
        self.sliderOffset.setCaptionLabel("ruleOffset").setRange(-1, 1)
        self.listSino.bringToFront()
        self.listHisto.bringToFront()
        self.listImage.bringToFront()