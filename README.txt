Introduction

This is a solution for the Integration Engineer Coding Challenge. The solution is built on python 2.7 and utilizes built-in libraries. The solution was tested in python 2.7.15 using standard python conventions, which should be portable for all 2.7+ versions and possibly extend to earlier versions such as 2.5 and 2.6. If there are errors, ensure your python installation base has the following libraries:

1. re - the standard built-in regular expression library
2. sys - the standard sys library (it is unlikely that this will be an issue)
3. xml.etree.ElemenTree - this is a third-party xml parsing library that is typically pre-installed on python 2.7.15

Note: if any of these libraries are missing, use the pipy command to install and/or repair the libraries. If pipy isn't available as a standalone script, you can try the module using python -m pipy install <library>. If neither of these work, attempt to install pypi from https://pypi.org/. 

Run Instructions

1. download the project
To download the use the following git command in the desired running path for this project

Example:
  c:\my_path\> git clone https://github.com/sdiaz29/-Integration-Engineer-Coding-Challenge

2. setting the xml file location. 
To run the solution simply edit the file and modify the fourth line containing variable "myfile" which points to the file we will be importing. Add the location of the xml file to be processed as a string value to this variable. Be sure to escape any characters that are in the path name which might cause a syntax error this includes forward slashes "/" which are popular in windows. When this change is complete, be sure to save and close the file.

Example:
  myfile = "c:\\project\\myfile.xml"
  
3. running the command
Once file is saved, simply execute the file using the following instructions:

Example:
c:\my_path\python\ challenge_answer.py
