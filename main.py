"""
This is just a starting document to get some foundational code layed out. Feel free to edit as you wish and make large revision, I just wanted to get things started. Good luck everyone!

Need to create geometry of the grid(s) as well as dimensions and boundary conditions
"""

#ION-I Optics grids simulations
import femm
import numpy as np



#Open FEMM and create electrostatic document
femm.openfemm()
femm.newdocument(1) # 1 denotes electrostatic problem
femm.ei_zoomnatural() # make sure to manually zoom to fully see everything



# Define problem: units, type='axi' for axisymmetric
# ei_probdef(units, type, precision, depth, minangle)
femm.ei_probdef('millimeters', 'axi', 1e-8, 1, 30)



#Parameters (can edit this to tweak our design)
ts = 0.5    # screen thickness (mm)
ta = 0.5    # accel thickness (mm)
g  = 2.0    # gap between grids (mm) (front face to front face)
Rs = 1.0    # screen hole radius (mm)
Ra = 0.7    # accel hole radius (mm)
Rout = 3.0  # outer radius of unit cell (mm)

V_screen = 0.0      # screen potential (V)
V_accel  = -1000.0  # accel potential (V)
