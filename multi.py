import sys, os
project_path = r'C:\Users\jpark\Desktop\PyProjects\MayaJointFixer'
sys.path.append(project_path)

import maya.cmds as cmds
import maya.mel as mel
from jointFix import jointFixLocalRotateAxis


targetList = [r'C:\Users\jpark\Desktop\New folder\Final_V1.ma', 
             r'C:\Users\jpark\Desktop\New folder\Final_V2.ma', 
             r'C:\Users\jpark\Desktop\New folder\Final_V3.ma']



for eachFile in targetList:
    directory, filename = os.path.split(eachFile)
    newFilename = filename.replace('Final_', 'Final_edited_')
    newPath = os.path.join(directory, newFilename)

    cmds.file(eachFile, open=True, force=True)

    jointFixLocalRotateAxis("Leg_Middle_Jnt_L", 180, 0, 0, "skinCluster4", "Body", "Root")

    cmds.file(rename=newPath)
    cmds.file(save=True, type='mayaAscii')




