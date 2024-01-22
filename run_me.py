# this needs to be run at the start of a Maya to even recognize other modules in this project
# however, maya will not recognize changes in other modules (ex. fileIterator.py) unless Maya is restarted

project_path = r'C:\Users\jpark\Desktop\PyProjects\MayaJointFixer'

import sys, os
sys.path.append(project_path)

from jointFix import jointFixLocalRotateAxis
import fileIterator as fi

targetList = [r'C:\Users\jpark\Desktop\New folder\Final_V1.ma', 
             r'C:\Users\jpark\Desktop\New folder\Final_V2.ma', 
             r'C:\Users\jpark\Desktop\New folder\Final_V3.ma']

# targetList = [r'C:\Users\jpark\Desktop\New folder\Final_V1.ma']


instance = fi.localRotationalAxisChangeSkinBound("jointfixed", targetList, "Leg_Middle_Jnt_L", 180, 0, 0, "skinCluster4", "Body", "Root")
instance.tester()


