import os, sys
# print(sys.path)
# project_path = r'C:\Users\jpark\Desktop\PyProjects\MayaJointFixer'
# sys.path.append(project_path)
import fileIterator
import pytest

targetList = [r'C:\Users\test\Desktop\New folder\Final_V1.ma', 
             r'C:\Users\test\Desktop\New folder\Final_V2.ma', 
             r'C:\Users\test\Desktop\New folder\Final_V3.ma']

dest = r'C:\Users\jpark\Desktop\New folder'

testName = r'C:\Users\test\Desktop\New folder\Final_V1.ma'


def test_editFileNameAndPath():
    testInstance = fileIterator.targetFiles(targetList, dest)
    result = testInstance.editFileNameAndPath("EDITED", testName)
    assert result == r'C:\Users\test\Desktop\New folder\Final_V1_EDITED.ma'

def test_editFileNameOnly():
    testInstance = fileIterator.targetFiles(targetList, dest)
    result = testInstance.editFileNameOnly("EDITED", testName)
    assert result == 'Final_V1_EDITED.ma'