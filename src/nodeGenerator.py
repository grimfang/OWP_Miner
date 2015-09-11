#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys
import random

### PANDA Imports ###


########################################################################

## Common Ores ##
# Copper
# Iron
# Silver
# Gold
#################

class NodeGenerator():

    def __init__(self, _main, _numOfNodes):
    	self.main = _main
    	self.numOfNodes = _numOfNodes
    	self.currentNodes = {}

    	self.generateNodes()
    	self.placeNodes()

    def generateNodes(self):
    	# Generate number of nodes
    	for x in range(self.numOfNodes):
    		self.currentNodes[x] = Node()

    def placeNodes(self):
    	for i in xrange(self.numOfNodes):
    		x = random.random() * self.main.t.terrainSize[0]
    		y = random.random() * self.main.t.terrainSize[1]

    		if random.random() < self.main.t.terrain.getElevation(x, y):
    			elevation = self.main.t.terrain.getElevation(x, y)
    			node = random.choice(self.currentNodes)
    			node.model.setPos(x, y, elevation*25)

    def respawnQueue(self):
    	pass



class Node():

	def __init__(self):
		types = ['copper', 'iron', 'silver', 'gold']

		self.type = random.choice(types)
		self.lootAmount = random.randint(1, 8)
		self.respawnTime = random.randint(300, 3600) # 5mins - 60mins, Maybe a bit heavy but whatever
		self.position = (0, 0, 0)
		self.model = None
		self.collisionShape = None

		self.model = loader.loadModel("ball")
		self.model.reparentTo(render)
		self.model.setPos(self.position)
		self.model.setScale(0.5)

	def setCollisionShape(self):
		pass

	def setModel(self):
		pass

	def setPosition(self):
		pass
