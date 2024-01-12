from fileIterator import targetFiles
from jointFix import jointFixLocalRotateAxis


targetList = [r'C:\Users\test\Desktop\New folder\Final_V1.ma', 
             r'C:\Users\test\Desktop\New folder\Final_V2.ma', 
             r'C:\Users\test\Desktop\New folder\Final_V3.ma']


instance = targetFiles(targetList)

instance.fileIterate("jointFixed", jointFixLocalRotateAxis, ["Leg_Middle_Jnt_L", 180, 0, 0, "skinCluster4", "Body", "Root"])