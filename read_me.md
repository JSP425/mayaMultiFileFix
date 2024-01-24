# Read Me

## About

This project aims to automatically manipulate multiple Maya files in one execution. 

The targeted files and the manipulation is dependent on the user.

Currently, there is only one manipulation that the project can perform but the intention is to build several useful functions as their need arises. 

The idea for this arose when I needed to change the local rotational axis of a skin bound rig and there were several versions of this rig. In a pipeline, this could be useful for making adjustments to rigs or other Maya files that have already gone downstream.

### Getting started

refer to the `run_me.py` example.

Make sure Maya's ports are configured to the external IDE.

To be able to run this properly, you will need to add the project path to sys.path at the start of execution. Otherwise, Maya will not be able to read from the other modules in this project and the script will fail. 

```python
import sys, os
project_path = r'C:\filepath\to\your\project\folder'
sys.path.append(project_path)
```

Afterwards, input the list of targeted file paths to iterate over 
```python
targetList = [r'C:\filepath\to\your\project\folder\Final_V1.ma', 
             r'C:\filepath\to\your\project\folder\Final_V2.ma', 
             r'C:\filepath\to\your\project\folder\Final_V3.ma']
```

Create an instance of the manipulation to apply.
The example below will target a joint called Leg_Middle_Jnt_L, turn it 180 degrees **relative** to its current orientation on the x-axis. More information is available in the method's docstrings for other the parameters. 

```python
instance = fi.localRotationalAxisChangeSkinBound("jointfixed", targetList, "Leg_Middle_Jnt_L", 180, 0, 0, "skinCluster4", "Body", "Root")
```

To execute the script, press `shift+alt+m` or right click on the script and press `Send Python Code to Maya`. 

The last file in the list list will be the one open. The manipulated files will be saved in the same directory of the original file, with the designated suffix. In the current example, you would have the files:

Final_V1_jointfixed, Final_V2_jointfixed and Final_V3_jointfixed all inside C:\filepath\to\your\project\folder

### Making Changes

If the user wants to make changes to other modules outside of `run_me.py` or wherever the user executes the script from, the user will need to restart Maya.

Docstrings need to be interpreted as a literal string otherwise Maya's script editor will throw an error:

Error: line 1: SyntaxError: file <string> line 11: (unicode error) 'unicodeescape' codec can't decode bytes in position 382-383: truncated \UXXXXXXXX escape

For that reason the docstring triple quotations are preceded by an r in this project. 

### Future Development Ideas

- The script currently edits an original file and then saves it under a new name; it would be safer to first save the file under a new name and then edit it. This would minimize/negate risk to the original files. 

- Give users the option to save the manipulated files in a specified/new directory; currently, the edited files will save in the same directory as the original.

