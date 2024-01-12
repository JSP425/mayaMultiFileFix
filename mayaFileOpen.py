# import maya.standalone
# maya.standalone.initialize(name='python')

import sys, os
project_path = r'C:\Users\jpark\Desktop\PyProjects\MayaJointFixer'
sys.path.append(project_path)

import maya.cmds as cmds
import maya.mel as mel
from jointFix import jointFixLocalRotateAxis


# File paths
input_file_path = r'C:\Users\jpark\Desktop\Captsone\Sabretooth\Sit\Final_V1.ma'
output_file_path = r'C:\Users\jpark\Desktop\Final_V1_edited.ma'



# Open the file
cmds.file(input_file_path, open=True, force=True)

jointFixLocalRotateAxis("Leg_Middle_Jnt_L", 180, 0, 0, "skinCluster4", "Body", "Root")

# Save the file
cmds.file(rename=output_file_path)
cmds.file(save=True, type='mayaAscii')

# Close Maya standalone
# maya.standalone.uninitialize()
