import rhinoscriptsyntax as rs

def getVertexString(point):
    return "v "+str(point[0])+" "+str(point[1])+" "+str(point[2])+"\n"
def getFaceString(indexes):
    faceString="f"
    for index in indexes:
        faceString=faceString+" "+str(index)
    return faceString+"\n"


polysurfaces=rs.GetObjects('select polysurfaces',16)
nU=rs.GetInteger("u",1)
nV=rs.GetInteger("v",1)
filename = rs.SaveFileName()
vertices={}
vI=1
# file = open("testPythonexport.obj", "w")
file = open(filename, "w")
for polysurface in polysurfaces:
    surfaces=rs.ExplodePolysurfaces( polysurface )
    for surface in surfaces:
        domainU = rs.SurfaceDomain(surface, 0)
        dU=(domainU[1]-domainU[0])/nU
        domainV = rs.SurfaceDomain(surface, 1)
        dV=(domainV[1]-domainV[0])/nV
        for i in range(nU):
            for j in range(nV):
                cU1=i*dU+domainU[0]
                cV1=j*dV+domainV[0]
                cU2=(i+1)*dU+domainU[0]
                cV2=(j+1)*dV+domainV[0]
                pt1=rs.SurfaceEvaluate (surface, [cU1,cV1], 1)[0]
                pt2=rs.SurfaceEvaluate (surface, [cU2,cV1], 1)[0]
                pt3=rs.SurfaceEvaluate (surface, [cU2,cV2], 1)[0]
                pt4=rs.SurfaceEvaluate (surface, [cU1,cV2], 1)[0]
                pts=[pt1,pt2,pt3,pt4]
                indexes=[]
                for point in pts:
                    index=vertices.get(point)
                    if index==None:
                        vertices[point]=vI
                        file.write(getVertexString(point))
                        index=vI
                        vI+=1
                    indexes.append(index)
                file.write(getFaceString(indexes))
                rs.AddCurve ([pt1,pt2,pt3,pt4], 1)
file.close()


