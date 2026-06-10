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
femm.ei_zoom(-5,-5,5,5) # Can adjust this if we change the grid radius. Rout = 3.0 at time of (-5,-5,5,5) implementation



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



#Function for easier segment and arc connection
def seg(x1, y1, x2, y2):
    femm.ei_addnode(x1, y1)
    femm.ei_addnode(x2, y2)
    femm.ei_addsegment(x1, y1, x2, y2)

def arc(x1, y1, x2, y2, angle, max_segments):
    femm.ei_addnode(x1, y1)
    femm.ei_addnode(x2, y2)
    femm.ei_addarc(x1, y1, x2, y2, angle, max_segments)



#Outer circle shape
'''
The old circle code before arc function
femm.ei_addnode(0, 0 + Rout)
femm.ei_addnode(0, 0 - Rout)
femm.ei_addarc(0, 0 + Rout, 0, 0 - Rout, 180, 1)
femm.ei_addarc(0, 0 - Rout, 0, 0 + Rout, 180, 1)
'''
arc(0,0+Rout,0,0-Rout,180,1) #New code using arc function
arc(0,0-Rout,0,0+Rout,180,1)



#Make grid the proper material (stainless steel 304)
femm.ei_addmaterial('stainless steel 304', 1, 1, 1e6) # NOT ACCURATE
#(name, permittivity_x, permittivity_y, conductivity)

# Add block label inside circle
femm.ei_addblocklabel(0.1 * Rout, 0)
femm.ei_selectlabel(0.1 * Rout, 0)

# Assign material to circle region
femm.ei_setblockprop("stainless steel 304", 1, 0, 0) # (name, automesh, meshsize, group)
femm.ei_clearselected()
femm.ei_refreshview()


