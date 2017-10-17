import pylab
import random

reg=[(random.normalvariate(i/4,0.1),random.normalvariate(i/4,0.1)) for i in range(20)]
		
pylab.figure()
pylab.plot([p[0] for p in reg],[p[1] for p in reg],'ro')
pylab.show()




