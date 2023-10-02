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

#Parse Data
# Copy and paste a line of data as the lineString variable value
lineString= "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

#Using the split command to parse the items in the lineString into a list object
lineData= lineString.split()

#Assign variaables to each item in the list
record_id = lineData[1]   #ARGOS Tracking record ID
obs_date = lineData[2]    #Observation date
ob_lc = lineData[3]       #Observation Location Class
obs_lat = lineData[7]     #Observation Latitude
obs_long = lineData[8]    #Observation Longitude

#Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_long}W on {obs_date}")
"""To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark in a print() statement. 
Inside this string, you can write a Python expression between { } characters that can refer to variables or literal values. 
It is an easier way to insert direct values with {} calling the variables rather than using a concatenation for every word"""
