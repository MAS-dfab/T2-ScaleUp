import hdgeom.mesh.renderer.Renderer as Renderer

class RendererGroup(Renderer):
    def getPShape(self,applet,mesh):
        colorDictionary={
            0: applet.color(255,0,0),
            1: applet.color(255,255,0),
            2: applet.color(255,0,255)
        }
        shape = applet.createShape(PConstants.GROUP)
        tris = applet.createShape()
        tris.beginShape(PConstants.TRIANGLES)
        tris.fill(applet.color(0,0,255))
       
        for face in mesh.faces:
            if face.getNumPoints() == 3:
                tris.fill(colorDictionary[face.group])
                for v in face.points:
                    tris.vertex(v.x, v.y, v.z)
        tris.endShape()
        shape.addChild(tris)

        quads = applet.createShape()
        quads.beginShape(PConstants.QUADS)
        quads.fill(applet.color(0,0,255))
        for face in mesh.faces:
            if face.getNumPoints() == 4:
                quads.fill(colorDictionary[face.group])
                for v in face.points:
                    quads.vertex(v.x, v.y, v.z)
        quads.endShape()
        shape.addChild(quads)
        
        return shape