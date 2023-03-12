import numpy as np
import pyrosim.pyrosim as pyrosim
import os

class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(3, 2) * 2 - 1
        self.fitness = 0

    def Evaluate(self):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system('python simulation.py')
        with open('fitness.txt', 'r') as f:
            self.fitness = float(f.readline())

    def Create_World(self):

        pyrosim.Start_SDF('world.sdf')

        length = 1
        width = 1
        height = 1

        x = -10
        y = 10
        z = 0.5

        pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])
        
        pyrosim.End()

    def Generate_Body(self):

        pyrosim.Start_URDF('body.urdf')
        
        # link dims
        length = 1
        width = 1
        height = 1

        # abs coords for torso
        x = 1.5
        y = 0
        z = 1.5

        pyrosim.Send_Cube(name='Torso', pos=[x, y, z], size=[length, width, height])
        pyrosim.Send_Joint(name = 'Torso_BackLeg' , parent= 'Torso' , child = 'BackLeg' , type = 'revolute', position = [1, 0, 1])
        pyrosim.Send_Cube(name='BackLeg', pos=[-0.5, y, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name = 'Torso_FrontLeg' , parent= 'Torso' , child = 'FrontLeg' , type = 'revolute', position = [2, 0, 1])
        pyrosim.Send_Cube(name='FrontLeg', pos=[0.5, y, -0.5], size=[length, width, height])

        pyrosim.End()

    def Generate_Brain(self):

        pyrosim.Start_NeuralNetwork("brain.nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for row in range(3):
            for col in range(2):
                pyrosim.Send_Synapse(
                    sourceNeuronName = row, 
                    targetNeuronName = col+3, 
                    weight = self.weights[row][col]
                )

        pyrosim.End()