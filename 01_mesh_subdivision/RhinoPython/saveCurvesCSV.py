import rhinoscriptsyntax as rs

curves=rs.GetObjects('select Lines',4)
filename = rs.SaveFileName()
file = open(filename, "w")

for curve in curves:
    layername=rs.ObjectLayer(curve)
    points = rs.CurvePoints(curve)
    file.write(layername+" ")
    for pt in points:
        file.write(str(pt[0])+","+str(pt[1])+" ")
    file.write("\n")
file.close()
