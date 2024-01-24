# Data Model

## Data Model Explanation

In this project, the data model is designed to automatically manipulate multiple Maya files and easily accomodate future manipulation methods into the project. 

## Design Rationale

Currently, the only manipulation available is to adjust a joint's local rotational axis after it has been skin bound. Normally, a single script executed in Maya's script editor would suffice. However, I anticipated that there may be future needs to perform other operations across multiple files; so I decided to set this up as a project to better organize the various scripts. Each manipulation will be its own module called by the module that iterates through the files, `fileIterator`. 

I also saw an opportunity to avoid repetitive code editing file paths, file names and open/closing/saving Maya files. Rather than having these general functions repeated across multiple manipulation scripts, I organized it so that child classes such as `localRotationalAxisChangeSkinBound` inherits from the parent class `targetFiles` who holds the general methods.

Because I wanted to run these scripts from a project folder, the user would execute their script from an external IDE. In addition to modifying the ports in Maya, the user will also need to do some other adjustments like adding the project folder to sys.path at the start of the script. This is elaborated in the read_me.md.



