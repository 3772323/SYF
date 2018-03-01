from gl_lib.sim.affichage.deuxD.interface import *
from gl_lib.sim.robotRep.RobotAutonome import *
from gl_lib.sim.affichage.deuxD.vue2DRep import *
from gl_lib.sim.geometrie3D.pointRep import *
from gl_lib.sim.robotRep.strategie.deplacement import *

r=RobotAutonome(Pave(50,50,0), Objet3D(), Objet3D(), Vecteur(0,-1,0))
r.stratDeplacement=DeplacementSimple(r)
r.deplacer(Vecteur(100,100,0))
a=Arene(400, 350)
a.add(r)

app=AppRobotAutonome(r, Vue2DArene(a))
app.init() 

app.mainloop()

