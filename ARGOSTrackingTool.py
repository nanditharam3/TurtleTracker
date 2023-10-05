#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2023
#--------------------------------------------------------------

#Create a variable pointing to the data file
filename = './Data/Raw/Sara.txt'

#Create a file object from the file
file_object = open(filename,'r')

#Read contents of file into a list
lineString = file_object.readline()

#Iterate through lines
while lineString:
    #Pretend we read all lines of data from the file using a for loop
        if lineString[0]=='#':
            lineString = file_object.readline()
            continue
        elif lineString[0]=='u':
            lineString = file_object.readline()
            continue
        else:
            #Split the string into a list of data items
            lineData = lineString.split()

            #Extract items in list into variables
            record_id = lineData[0]
            obs_date = lineData[2]
            obs_lc = lineData[4]
            obs_lat = lineData[6]
            obs_lon = lineData[7]

            #Move to next line
            lineString=file_object.readline()

#Close the file
file_object.close()

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

"""To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark in a print() statement. 
Inside this string, you can write a Python expression between { } characters that can refer to variables or literal values. 
It is an easier way to insert direct values with {} calling the variables rather than using a concatenation for every word"""
