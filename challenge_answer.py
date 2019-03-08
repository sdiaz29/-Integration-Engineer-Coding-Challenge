import re #import regular expression library
import sys #import sys for the sys.stdout.write command with 
import xml.etree.ElementTree as ET #import xml library to parse xml document

myfile = "path_of_file" #set path of file
tree = ET.parse(myfile)
root = tree.getroot()

#iterate through the xml extracting individual members

for child in root:
    first_name = ""
    last_name = ""
    full_name = ""

    sys.stdout.write("\t{\n")

    #iterate through each sub member of the xml to extract individual fields
    
    for i,grandChild in enumerate(child):
        fieldList = [("first_name", "firstName"), ("last_name", "lastName"), ("member_full", "fullName"), ("bioguide_id","chartid"), ("phone", "mobile"), ("address", "address")]
        fieldName = ""
        fieldMatch = False
        addrFlag = False

        #iterate through the field list matching on the desired fields and converting them to the names we want to use in our JSON     
        
        for f in fieldList:
            if(grandChild.tag == f[0]):
                fieldMatch = True
                fieldName = f[1]
            break

        #match only on the fields that we need    
            
        if fieldMatch:

            #test for field names for address, chartid, and others
            
            if fieldName == "address":

                #print the address field name
                
                sys.stdout.write("\t\t\""+ fieldName +"\":[\"" + '\n\t\t{' + "\n" )
                
                #extract street, city, state, and postal code using regex
        
                street = re.search(r'^\w?\d+[\S\s&]*?\s(?:\w+\s){2,4}', grandChild.text, re.M).group()
                city = re.search(r'(\w+)\s\w{2}\s+\d+\s*?$', grandChild.text, re.M).group(1)
                state = re.search(r'(\w{2})\s+\d+\s*?$', grandChild.text).group(1)
                postal = re.search(r'\d+\s*?$', grandChild.text).group()

                #print elements for street, city, state, and postal code
                
                sys.stdout.write("\t\t\t\""+ "street" +"\":\"" + street + "\"" + ",\n" )
                sys.stdout.write("\t\t\t\""+ "city" +"\":\"" + city + "\"" + ",\n" )
                sys.stdout.write("\t\t\t\""+ "state" +"\":\"" + state + "\"" + ",\n" )
                sys.stdout.write("\t\t\t\""+ "postal" +"\":\"" + postal + "\"" + "\n" )
                sys.stdout.write("\t\t ]\n")
                sys.stdout.write("\t\t},\n")
                
            elif fieldName == "chartid":
                sys.stdout.write("\t\t\""+ fieldName +"\":\"" + grandChild.text + "\"" + "\n" )
            else:    
                sys.stdout.write("\t\t\""+ fieldName +"\":\"" + grandChild.text + "\"" + ",\n" )

    #print the trailing curly brace for each member
    sys.stdout.write("\t}\n")
