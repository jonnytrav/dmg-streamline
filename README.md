### THIS FILE WILL BE USED TO DOCUMENT EDGE CASE UNCOMMON ERRORS AND HOW THEY WERE SOLVED, ALONG WITH CRUCIAL STEPS TO SET UP ENVIRONMENT AND DEPENDENCIES ###

Problem: Import "pandas" could not be resolved from source Pylance.

Solution: The python3 interpreter version from the terminal must be the same as our python version selection in VSCode. Type "python3" into terminal and the response should contain the version of python being used. Then, in VSCode, in the bottom right corner of the window (a python file must be open for this to be available), you will seet the version of python being used. Click to open a drop down and select the version that matches the version with which your terminal responded.
#
Problem: XLWings is not appearing in Excel ribbon after install.

Solution: Manually install XLWings add-in by double-clicking the .xlam file located in the addin directory within python's folder ("C:\Python310\Lib\site-packages\xlwings\addin" in my local system)
