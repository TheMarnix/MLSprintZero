import network
import mnist_loader
import numpy as np
from random import randint, shuffle
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

training_data=[]
test_data=[]
for i in range(1000):
	training_data.append([np.array([[randint(0, 9)],[randint(0, 9)]]),np.array([[1],[0]])])
	training_data.append([np.array([[randint(90, 99)],[randint(90, 99)]]),np.array([[0],[1]])])
	if i%10:
		test_data.append([np.array([[randint(0, 9)],[randint(0, 9)]]),np.array([[1],[0]])])
		test_data.append([np.array([[randint(90, 99)],[randint(90, 99)]]),np.array([[0],[1]])])

shuffle(training_data)
shuffle(test_data)

print(test_data[0])

net = network.Network([2, 3, 2])
net.SGD(training_data, 30, 1, 0.01, test_data=test_data)