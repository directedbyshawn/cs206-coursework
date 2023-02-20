import numpy as np

ITERATIONS = 1000

# Motor control settings for back leg
amplitudeBL = np.pi/8
frequencyBL = 10
phaseOffsetBL = 0

# Motor control settings for front leg
amplitudeFL = np.pi/8
frequencyFL = 10
phaseOffsetFL = np.pi/4

max_force = 500

sleep = 1/60