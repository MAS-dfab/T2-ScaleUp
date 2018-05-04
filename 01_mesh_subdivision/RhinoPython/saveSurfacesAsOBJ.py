import rhinoscriptsyntax as rs

def getVertexString(point):
    return "v "+str(point[0])+" "+str(point[1])+" "+str(point[2])+"\n"
def getFaceString(indexes):
    faceString="f"
    for index in indexes:
        faceString=faceString+" "+str(index)
    return faceString+"\n"

def getFaceStringComment(indexes,comment):
    faceString="f"
    for index in indexes:
        faceString=faceString+" "+str(index)
    return faceString+" # "+str(comment)+"\n"

def saveSurfaceBorders():
    surfaces=rs.GetObjects('select surfaces',8)
    filename = rs.SaveFileName()
    vI=1
    file = open(filename, "w")
    for surface in surfaces:
        layername=rs.ObjectLayer(surface)
        border=rs.DuplicateSurfaceBorder(surface)
        pts=rs.CurvePoints(border)
        pts=pts[:-1]
        indexes=[]
        for point in pts:
            file.write(getVertexString(point))
            indexes.append(vI)
            vI+=1
        file.write(getFaceStringComment(indexes,layername))
        # file.write(getFaceString(indexes))
        rs.DeleteObject(border)
    file.close()
    return

def saveSurfacesQuadDomains():
    surfaces=rs.GetObjects('select surfaces',8)
    nU=rs.GetInteger("u",2)
    nV=rs.GetInteger("v",2)
    filename = rs.SaveFileName()
    vertices={}
    vI=1
    # file = open("testPythonexport.obj", "w")
    file = open(filename, "w")

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

#saveSurfaceBorders()
saveSurfacesQuadDomains()
