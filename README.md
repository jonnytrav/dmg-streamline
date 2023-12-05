### THIS FILE WILL BE USED TO DOCUMENT EDGE CASE UNCOMMON ERRORS AND HOW THEY WERE SOLVED, ALONG WITH CRUCIAL STEPS TO SET UP ENVIRONMENT AND DEPENDENCIES ###

Problem: Import "pandas" could not be resolved from source Pylance.
Solution: The python3 interpreter version from the terminal must be the same as our python version selection in VSCode. Type "python3" into terminal and the response should contain the version of python being used. Then, in VSCode, in the bottom right corner of the window (a python file must be open for this to be available), you will seet the version of python being used. Click to open a drop down and select the version that matches the version with which your terminal responded.

