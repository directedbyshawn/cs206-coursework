import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF('body.urdf')
        self.nn = NEURAL_NETWORK('brain.nndf')
        self.motors = {}
        self.sensors = {}
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, step):
        for sensor in self.sensors.values():
            sensor.Get_Value(step)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Act(self, step):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                for motor in self.motors.values():
                    if motor.jointName.decode('utf-8') == jointName:
                        motor.Set_Value(self.robotId, desiredAngle)

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        x = positionOfLinkZero[0]
        y = positionOfLinkZero[1]
        z = positionOfLinkZero[2]
        with open('fitness.txt', 'w') as f:
            f.write(str(x))