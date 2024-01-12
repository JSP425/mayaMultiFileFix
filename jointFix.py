import maya.cmds as cmds
import maya.mel as mel

# joint = "Leg_Middle_Jnt_L"
# xValue = -180
# yValue = 0
# zValue = 0
# targetSkinCluster = "skinCluster4"
# targetMesh = "Body"
# skeletonRoot = "Root"

def jointFixLocalRotateAxis(joint, xValue, yValue, zValue, targetSkinCluster, targetMesh, skeletonRoot) -> None:
    """
    Changes the local rotational axis relative to its current values for joints already bound to skin

    The old mesh will be duplicated and the new mesh will have the skin weights copied from the previous
    The old mesh will be hidden rather than deleted
    
    """
    # set local rotation axis as true for componen selection
    cmds.selectType(localRotationAxis=True)

    # select target joint
    # joint=cmds.ls(sl=True)[0]
    cmds.select(joint+".rotateAxis")
    cmds.rotate(xValue, yValue, zValue, relative=True,objectSpace=True,forceOrderXYZ=True)
    mel.eval("joint -e -zso Leg_Middle_Jnt_L;")

    # set evelope of original/effected mesh to 0
    cmds.setAttr(f"{targetSkinCluster}.envelope",0)
    duplicateName = cmds.duplicate(targetMesh, n=f"{targetMesh}_new")
    cmds.hide(targetMesh)

    # bind skeleton from root to new mesh
    cmds.select(skeletonRoot)
    # cmds.select("Body1",add=True)
    cmds.select(duplicateName, add=True)
    cmds.SmoothBindSkin()

    # optional: copy skin weights from original mesh to new
    cmds.select(targetMesh)
    cmds.select(duplicateName,add=True)
    cmds.copySkinWeights(noMirror=True, surfaceAssociation="closestPoint", influenceAssociation="closestJoint")

# jointFixLocalRotateAxis()