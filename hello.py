import re

string = "Assignment Number=484537 Employee Name=John Smith Location=London\n Assignment Number=859375 Employee Name=Fatima Ali Role=Manager\n"
fields = ["Assignment Number","Employee Name","Location","Role"]
separator = "="
def text2json(fields,string,separator):
    field_count = len(fields)
    record_count = string.count(fields[0])
    dict1 = {}
    dict2 = {}
    indices_list = []
    joined_indices = []
    
    #create indices list of lists for where each field occurs in the string
    for i in range(0,field_count):    
        indices_list.append([m.start() for m in re.finditer(fields[i], string)])
    
    
    for i in range(0,len(indices_list)):
        x = indices_list[i]
        for j in range(0,len(x)):
            joined_indices.append(x[j])
            
    joined_indices = sorted(joined_indices)
        
    
    
    #joined_indices = [joined_indices.append() for x in indices_list]
    
    
    #create a dictionary with the fields as keys but empty values (with which to populate the outermost dictionary with records)
    for i in range(0,field_count):
        dict2[fields[i]] = ""
        
    #populate the outermost dictionary with records (dictionaries)
    for i in range(0,record_count):
        dict1[i] = dict2
    
    for i in range(0,record_count-1,1):
        for j in range(0,field_count-1,1):
            if fields[j] in dict2.keys():
                
                start_ind = indices_list[j][i]+len(fields[j])+1
                
                stop_ind =  joined_indices[joined_indices.index(indices_list[j][i]) + 1] - 1
                dict1[i][fields[j]] = string[start_ind:stop_ind]
    

    
    #print (fields)
    ##print (string)
    #print (separator)
    #print (record_count)
    print (dict1)
    print (dict2)
    print (indices_list)
    print (joined_indices)


text2json(fields,string,separator)
