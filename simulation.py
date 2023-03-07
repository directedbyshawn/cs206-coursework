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
        p.setGravity(0,0, c.GRAV)
        self.world = WORLD()
        self.robot = ROBOT()
        
    def __del__(self):
        p.disconnect()

    def Run(self):
        for step in range(c.ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(step)
            self.robot.Think()
            self.robot.Act(step)
            t.sleep(c.sleep)

        if c.SAVE_MOTOR_VALUES:
            for motor in self.robot.motors.values():
                motor.Save_Values()

        if c.SAVE_SENSOR_VALUES:
            for sensor in self.robot.sensors.values():
                sensor.Save_Values()
                

if __name__ == "__main__":
    simulation = SIMULATION()
    simulation.Run()
        