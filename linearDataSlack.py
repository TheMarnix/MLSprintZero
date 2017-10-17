import pylab
import random

classA=[(random.normalvariate(-1.5,1),random.normalvariate(0.5,1)) for i in range(5)]+[(random.normalvariate(1.5,1),random.normalvariate(0.5,1)) for i in range(5)]
classB=[(random.normalvariate(0,0.5),random.normalvariate(-0.5,0.5)) for i in range(5)]

labels=[1 for i in range(len(classA))]+[-1 for i in range(len(classB))]
		
pylab.figure()
pylab.plot([p[0] for p in classA],[p[1] for p in classA],'bo')
pylab.plot([p[0] for p in classB],[p[1] for p in classB],'ro')
pylab.show()

