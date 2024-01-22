import os
import maya.cmds as cmds
import maya.mel as mel

from jointFix import jointFixLocalRotateAxis

class targetFiles:
    """
    Parent class holding general methods for child classes
    not intended to be instanced
    
    """

    def __init__(self, editTag: str,filePathList: list) -> None:
        self.filePathList = filePathList
        self.editTag = editTag

    def editFileNameAndPath(self, editName: str, filePath: str):
        """
        Returns the specified file path with a new file name suffix.

        Used to preserve original file and create an edited version.
        Useful for creating the new edited file in the same directory as the original file
        
        editName: the new file suffix you want; ex. 'edited' -> Rig_V1 -> Rig_V1_edited
        filePath: the full original filepath; ex. r'C:\Users\someone\Desktop\projectFolder\Rig_V1.ma'
        returns: r'C:\Users\someone\Desktop\projectFolder\Rig_V1_edited.ma'
        
        """
        directory, filename = os.path.split(filePath)
        name, extension = os.path.splitext(filename)
        newFileName = f"{name}_{editName}{extension}"
        newFilePath = os.path.join(directory, newFileName)
        return newFilePath
    
    def editFileNameOnly(self, editName, filePath):
        """
        Returns the specified file name with an added suffix

        Used to add the new file name to a directory.
        Useful for creating the new edited file in a new location different from original

        editName: the new file suffix you want; ex. 'edited' -> Rig_V1 -> Rig_V1_edited
        
        """
        directory, filename = os.path.split(filePath)
        name, extension = os.path.splitext(filename)
        newFileName = f"{name}_{editName}{extension}"
        return newFileName
    
    def fileIterate(self, operation, values):
        """
        Iterates through multiple files with a specified operation

        Not intended to be used directly in an instance.
        A child class will utilize this method and input the values accordingly.
        
        """
        for eachFile in self.filePathList:
            cmds.file(eachFile, open=True, force=True)

            operation(*values)

            # self.editFileNameAndPath(editName, filePath)
            cmds.file(rename=self.editFileNameAndPath(self.editTag, eachFile))
            cmds.file(save=True, type='mayaAscii')

    def tester(self):
        print("======TESTER2=======")


class localRotationalAxisChangeSkinBound(targetFiles):
    """
    Changes the local rotational axis relative to its current values for joints already bound to skin

    The old mesh will be duplicated and the new mesh will have the skin weights copied from the previous
    The old mesh will be hidden rather than deleted

    editName: the new file suffix you want; ex. 'edited' -> Rig_V1 -> Rig_V1_edited
    filePath: the full original filepath; ex. r'C:\Users\someone\Desktop\projectFolder\Rig_V1.ma'
    returns: r'C:\Users\someone\Desktop\projectFolder\Rig_V1_edited.ma'
    
    targetSkinCluster: refers to the name of the input skin cluster binding the targeted joint; ex. 'skinCluster4'
    targetMesh: refers to the name of the mesh that is binding the targeted joint
    skeletonRoot: refers to the name of the root joint in the joint hierarchy
    
    """

    def __init__(self, editTag: str, filePathList: list, joint: str, xValue: float, yValue: float, zValue: float, targetSkinCluster: str, targetMesh: str, skeletonRoot: str) -> None:
        # super().__init__(editTag, filePathList)
        self.joint = joint
        self.xValue = xValue
        self.yValue = yValue
        self.zValue = zValue
        self.targetSkinCluster = targetSkinCluster
        self.targetMesh = targetMesh
        self.skeletonRoot = skeletonRoot
        super().__init__(editTag, filePathList) 

        self.inputValues = (self.joint, self.xValue, self.yValue, self.zValue, self.targetSkinCluster, self.targetMesh, self.skeletonRoot)

        # print(f"========{self.editTag, self.filePathList}")



