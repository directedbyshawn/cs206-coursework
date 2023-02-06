import pyrosim.pyrosim as pyrosim

def Create_World():

    pyrosim.Start_SDF('world.sdf')

    length = 1
    width = 1
    height = 1

    x = -10
    y = 10
    z = 0.5

    pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])
    
    pyrosim.End()

def Create_Robot():

    pyrosim.Start_URDF("body.urdf")
    
    # link dims
    length = 1
    width = 1
    height = 1

    # abs coords for torso
    x = 1.5
    y = 0
    z = 1.5

    pyrosim.Send_Cube(name='Torso', pos=[x, y, z], size=[length, width, height])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])
    pyrosim.Send_Cube(name='BackLeg', pos=[-0.5, y, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name='FrontLeg', pos=[0.5, y, -0.5], size=[length, width, height])
    

    pyrosim.End()

if __name__ == "__main__":
    Create_World()
    Create_Robot()