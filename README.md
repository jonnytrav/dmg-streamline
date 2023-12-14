### THIS FILE WILL BE USED TO DOCUMENT EDGE CASE UNCOMMON ERRORS AND HOW THEY WERE SOLVED, ALONG WITH CRUCIAL STEPS TO SET UP ENVIRONMENT AND DEPENDENCIES ###

Problem: Import "pandas" could not be resolved from source Pylance.

Solution: The python3 interpreter version from the terminal must be the same as our python version selection in VSCode. Type "python3" into terminal and the response should contain the version of python being used. Then, in VSCode, in the bottom right corner of the window (a python file must be open for this to be available), you will seet the version of python being used. Click to open a drop down and select the version that matches the version with which your terminal responded.
#
Problem: XLWings is not appearing in Excel ribbon after install.

Solution: Manually install XLWings add-in by double-clicking the .xlam file located in the addin directory in python's installation folder ("C:\Pythonx\Lib\site-packages\xlwings\addin" in my local system).
#
Problem: XLWings disappears from Excel ribbon after Excel is closed and reopened.

Solution: File -> Options -> Add-ins - At the bottom of the window there should be a drop-down menu next to the word "Manage", and "Excel Add-ins" must be checked for this to work. Then click  "Go..." (should be right next to drop-down menu) to open the Add-ins dialog box. Click "Browse" and navigate to the xlwings add-in (.xlam) file within the Python installation's "...\Lib\site-packages\xlwings" directory or the "Lib\site-packages\xlwings\addin" directory. Select the file and click "OK". Then, after you're returned to the Add-ins dialog box, in the Add-ins available list, ensure that the "Xlwings" box is checked. Click OK to close the Add-ins dialog box. Make sure to save workbook so the XLWings add-in remains in the ribbon. Close book and restart Excel to confirm this worked correctly. 