import os
import maya.cmds as cmds
import maya.mel as mel


class targetFiles():

    def __init__(self, filePathList: list) -> None:
        self.filePathList = filePathList

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
    
    def fileIterate(self, editName, operation, values):
        for eachFile in self.filePathList:
            cmds.file(eachFile, open=True, force=True)

            operation(*values)

            # self.editFileNameAndPath(editName, filePath)
            cmds.file(rename=self.editFileNameAndPath(editName, eachFile))
            cmds.file(save=True, type='mayaAscii')

