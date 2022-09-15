import csv

#Open output file:
result = open('brca_cnvs_tcga_sol.csv', 'w')
writer = csv.writer(result)

#Open original csv:
with open('brca_cnvs_tcga-1.csv') as original:
    
    #read contents of the original csv
    reader = csv.reader(original)
    
    #Add length to data lines 
    for i in reader:
        #Check if header or normal row
        if 'ID' in i:
        
            #Create header separately as it differs from the other rows
            i.append('length')
            writer.writerow(i)
            
        else:
            #Generate length variable
            num1 = int(i[3])
            num2 = int(i[2])
            length = num1 - num2
            #Write the new line and add to output
            i.append(length)
            writer.writerow(i)
                
                
#Close output file
result.close()