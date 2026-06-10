"""
This is just a starting document to get some foundational code layed out. Feel free to edit as you wish and make large revision, I just wanted to get things started. Good luck everyone!

Need to create geometry of the grid(s) as well as dimensions and boundary conditions

This is a crude simulation setup with only one center hole in each of the grids. This is due to FEEM being a 2D application. We could also simulate each plate separately
and make them more detailed if we switched to planar mode
"""

#ION-I Optics grids simulations
import femm
import numpy as np



#Open FEMM and create electrostatic document
femm.openfemm()
femm.newdocument(1) # 1 denotes electrostatic problem
femm.ei_zoom(-1,-1,2,3) 



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



#Functions for adding segments easier
#Helper: add a vertical segment (grid wall or hole wall)
def vseg(r, z1, z2):
    femm.ei_addnode(r, z1)
    femm.ei_addnode(r, z2)
    femm.ei_addsegment(r, z1, r, z2)

#Helper: add a horizontal segment (top/bottom of plate)
def hseg(r1, r2, z):
    femm.ei_addnode(r1, z)
    femm.ei_addnode(r2, z)
    femm.ei_addsegment(r1, z, r2, z)


'''
Screen Grid
'''

#Hole wall
vseg(Rs, 0, ts)

#Metal region
vseg(Rout, 0, ts)

# Top and bottom faces
hseg(Rs, Rout, 0)     # bottom face
hseg(Rs, Rout, ts)    # top face


'''
Accelerator Grid
'''

# Hole wall
vseg(Ra, g, g + ta)

# Metal region
vseg(Rout, g, g + ta)

# Top and bottom faces
hseg(Ra, Rout, g)
hseg(Ra, Rout, g + ta)
