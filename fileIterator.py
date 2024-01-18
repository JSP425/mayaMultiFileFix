import os
import maya.cmds as cmds
import maya.mel as mel

from jointFix import jointFixLocalRotateAxis

class targetFiles:

    def __init__(self, editTag: str,filePathList: list) -> None:
        self.filePathList = filePathList
        self.editTag = editTag

    def editFileNameAndPath(self, editName, filePath):
        directory, filename = os.path.split(filePath)
        name, extension = os.path.splitext(filename)
        newFileName = f"{name}_{editName}{extension}"
        newFilePath = os.path.join(directory, newFileName)
        return newFilePath
    
    def editFileNameOnly(self, editName, filePath):
        directory, filename = os.path.split(filePath)
        name, extension = os.path.splitext(filename)
        newFileName = f"{name}_{editName}{extension}"
        return newFileName
    
    def fileIterate(self, operation, values):
        print("hi")
        for eachFile in self.filePathList:
            cmds.file(eachFile, open=True, force=True)

            operation(*values)

            # self.editFileNameAndPath(editName, filePath)
            cmds.file(rename=self.editFileNameAndPath(self.editTag, eachFile))
            cmds.file(save=True, type='mayaAscii')

    def tester(self):
        print("======TESTER2=======")


class jointFix(targetFiles):


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



