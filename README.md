### THIS FILE WILL BE USED TO DOCUMENT EDGE CASE UNCOMMON ERRORS AND HOW THEY WERE SOLVED, ALONG WITH CRUCIAL STEPS TO SET UP ENVIRONMENT AND DEPENDENCIES ###
Python Setup: python.org/downloads will contain links to download the latest LTS version of Python. If given the option to add this installation to your PATH, you should. That will make it much easier to access it from various locations. A couple windows will pop up throughout the download process and you should pretty much give it any permissions it asks for during. Pip, a dependency we need to manage other dependencies, should automatically be installed with Python.
#
XLWings Setup: Run the Command Prompt as an administrator and type "pip install xlwings" then press enter. The response should be something like "Successfully installed xlwings-0.30.13". To install the addin, enter command "xlwings addin install" once you've successfully installed XLWings.
#
Problem: Import "pandas" could not be resolved from source Pylance.

Solution: The python3 interpreter version from the terminal must be the same as our python version selection in VSCode. Type "python3" into terminal and the response should contain the version of python being used. Then, in VSCode, in the bottom right corner of the window (a python file must be open for this to be available), you will seet the version of python being used. Click to open a drop down and select the version that matches the version with which your terminal responded.
#
Problem: XLWings is not appearing in Excel ribbon after install.

Solution: After installing XLWings via the Command Prompt, you must install the addin via the "xlwings addin install" command now available to you. If it still does not appear in your Excel ribbon, manually launch XLWings add-in by double-clicking the .xlam file located in the "addin" directory within python's installation folder ("C:\Python310\Lib\site-packages\xlwings\addin" in my local system).
#
Problem: XLWings disappears from Excel ribbon after Excel is closed and reopened.

Solution: File -> Options -> Add-ins - then the bottom of the window there should be a drop-down menu next to the word "Manage" with the "Excel Add-ins" option selected for this to work. Then click  "Go..." (should be right next to drop-down menu) to open the Add-ins dialog box. Click "Browse" and navigate to the xlwings add-in (.xlam) file within the "addin" directory ("C:\Python310\Lib\site-packages\xlwings\addin" in my local system). Select the file and click "OK". Then, after you're returned to the Add-ins dialog box, in the "Add-ins available" list, ensure that the Xlwings box is checked. Click OK to close the Add-ins dialog box. Make sure to save workbook so the XLWings add-in remains in the ribbon. Close book and restart Excel to confirm this worked correctly.