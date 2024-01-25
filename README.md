### THIS FILE WILL BE USED TO DOCUMENT EDGE CASE UNCOMMON ERRORS AND HOW THEY WERE SOLVED, ALONG WITH CRUCIAL STEPS TO SET UP ENVIRONMENT AND DEPENDENCIES ###
Python Setup: The Anaconda distribution of Python automatically installs necessary packages like Xlwings and Pandas. https://www.anaconda.com/download will contain links to download the latest LTS version. Documentation for each install can be found at https://docs.anaconda.com/free/anaconda/install/windows/ (for Windows) https://docs.anaconda.com/free/anaconda/install/mac-os/ (for MacOS).
Doing this correctly should avoid below errors!
#
Problem: Import "pandas" could not be resolved from source Pylance. This can happen in VSCode but not really in Jupyter Notebook.

Solution: The python3 interpreter version from the terminal must be the same as our python version selection in VSCode. Type "python3" into terminal and the response should contain the version of python being used. Then, in VSCode, in the bottom right corner of the window (a python file must be open for this to be available), you will see the version of python being used. Click to open a drop down and select the version that matches the version with which your terminal responded.
#
Problem: XLWings is not appearing in Excel ribbon after install.

Solution: Would likely happen after installing Xlwings via the Command Prompt (not recommended, please use the Anaconda distribution of Python to get access to Xlwings). You must install the addin via the "xlwings addin install" command now available to you. If it still does not appear in your Excel ribbon, manually launch Xlwings add-in by double-clicking the .xlam file located in the "addin" directory within python's installation folder (most likely "C:\PythonXX\Lib\site-packages\xlwings\addin" in your local system).
#
Problem: Xlwings disappears from Excel ribbon after Excel is closed and reopened.

Solution: File -> Options -> Add-ins - then the bottom of the window there should be a drop-down menu next to the word "Manage" with the "Excel Add-ins" option selected for this to work. Then click  "Go..." (should be right next to drop-down menu) to open the Add-ins dialog box. Click "Browse" and navigate to the xlwings add-in file (with .xlam extension) within the "addin" directory ("C:\PythonXX\Lib\site-packages\xlwings\addin" in your local system). Select the file and click "OK". Then, after you're returned to the Add-ins dialog box, in the "Add-ins available" list, ensure that the Xlwings box is checked. Click OK to close the Add-ins dialog box. Make sure to save your workbook so the XLWings add-in remains in the ribbon. Close the book and restart Excel to confirm this worked correctly.