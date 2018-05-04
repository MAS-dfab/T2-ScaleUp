from Grid import GridList

def setup():
    size(1000,500)
    global img, agent, gridList,agents, mcSquare
    img = loadImage("structureBlur.jpg")
    agents=[]
    initField()
    for i in range(1000):
        addAgent(random(img.width),random(img.height))
        
def draw():
    scale(2)
    image(img,0,0)
    for agent in agents:
        agent.move()
        agent.display()

def addAgent(x,y):
    global agents
    agent=Agent(x,y,4,gridList)
    agent.color=color(255,0,0)
    if random(1)>0.5:
        agent.color=color(0,255,0)
        agent.walksGradient=False
    agents.append(agent)
    
def initField():
    global gridList,gridList2
    gridList=GridList(img.width,img.height)
    for x in range(img.width):
        for y in range(img.height):
            dir=PVector()
            cb=brightness(img.get(x,y))
            nNbs=0
            for xNb in range(-1,2):
                for yNb in range(-1,2):
                    if gridList.isInside(x+xNb,y+yNb):
                        b=brightness(img.get(x+xNb,y+yNb))
                        deltaB=b-cb
                        dir.add(xNb*deltaB,yNb*deltaB,0)
                        nNbs+=1
            dir.div(nNbs)
            dir.mult(-1.0)
            gridList.set(x,y,dir)
            
    
def mousePressed():
    addAgent(mouseX/2,mouseY/2)
    
class Agent:
    def __init__(self,x,y,speed,gridList):
        self.pos=PVector(x,y)
        self.speed=speed # linelength
        self.force=gridList.get(int(x),int(y)).copy()
        self.force.setMag(speed)
        self.points=[]
        self.gridList=gridList
        self.interia=0.8 # high value: abrupt direction change, otherwise damped
        self.color=color(255,0,0)
        self.walksGradient=True
    def move(self):
        direction=self.gridList.get(int(self.pos.x),int(self.pos.y)).copy()
        if self.walksGradient==False:# rotate vector 90 deg
            temp=direction.x
            direction.x=-direction.y
            direction.y=temp
        #if angle btwn direction and force bigger then 180 then inverse the direction
        if abs(PVector.angleBetween(direction, self.force))>PI/2.0:
                direction.mult(-1)
        direction.setMag(self.speed*self.interia)
        
        self.force.add(direction)
        self.force.setMag(self.speed)
        nextPos=self.pos.copy()
        nextPos.add(self.force)
        if (self.gridList.isInside(nextPos.x,nextPos.y)):
            self.pos=nextPos
            self.points.append(self.pos)
        
    def display(self):
        # print self.x
        strokeWeight(0.2)
        stroke(self.color)
        #rect(self.x,self.y,4,4)
        for  i in range(len(self.points)-1):
            p1=self.points[i]
            p2=self.points[i+1]
            line(p1.x,p1.y,p2.x,p2.y)
        if len(self.points)>200:
            self.points.pop(0)
            
            
    