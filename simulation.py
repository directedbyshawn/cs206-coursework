from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time as t

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        

    def __del__(self):
        p.disconnect()

    def Run(self):
        for step in range(c.ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(step)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = simulation.robot.robotId,
            #     jointName = b'Torso_BackLeg',
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAnglesBL[i],
            #     maxForce = c.max_force
            # )
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = simulation.robot.robotId,
            #     jointName = b'Torso_FrontLeg',
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAnglesFL[i],
            #     maxForce = c.max_force
            # )
            t.sleep(c.sleep)
                
        