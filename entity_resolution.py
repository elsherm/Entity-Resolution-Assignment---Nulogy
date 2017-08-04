# -*- coding: cp1252 -*-
import csv
import re
# Adding csv module to handle csv files and manipulations
# Adding re module to substitute special characters in title fields

with open('C:\Users\mohamed\Downloads\Scholar.csv', 'rU') as Scholarcsvfile:
    Scholarreader = csv.reader(Scholarcsvfile, delimiter=',')
    Scholarwriter = csv.writer(open('Scholar_clean.csv', 'wb'), delimiter = ',')
    Scholarwriterlog = csv.writer(open('Scholar_missingdata.csv', 'wb'), delimiter = ',')

# removing Empty Scholar IDs
# removing special characters from title fields
# converting title to UPPERCASE for comparisons later on
    for row in Scholarreader:
         if (len(row[0]) <=1):
             Scholarwriterlog.writerow(row)                                             # Write a log file for all the rows with empty Scholar IDs
         row[1]=re.sub(r'[-"/\.$?í€Œ¢í¢Œåí‰,ƒ\]\[ \t]', '', row[1])                     # removing all special characters from title field
         row[1] = str.upper(row[1])                                                     # converting title to UPPERCASE for comparisons later on
         Scholarwriter.writerow(row)                                                    # Writing the rows to a new clean file

Scholarcsvfile.close()

with open('C:\Users\mohamed\Downloads\DBLP1.csv', 'rU') as DBLPcsvfile:

     DBLPreader = csv.reader(DBLPcsvfile, delimiter=',')
     DBLPwriterlog = csv.writer(open('DBLP_duplicatedata.csv', 'wb'), delimiter = ',')
     DBLPwriter = csv.writer(open('DBLP_clean.csv', 'wb'), delimiter = ',')
     
# Removing Duplicates in DBLP1 based on title, author,and year
     entries=set()
     for row in DBLPreader:
        key = (row[1], row[2], row[4])
        if key in entries:
            DBLPwriterlog.writerow(row)

        row[1]=re.sub(r'[-"/\.$?í€Œ¢í¢Œåí‰,ƒ\]\[ \t]', '', row[1])                      # removing all special characters from title field
        row[1] = str.upper(row[1])                                                      # converting title to UPPERCASE for comparisons later on
        entries.add(key)
        DBLPwriter.writerow(row)                                                        # Writing the rows to a new clean file

DBLPcsvfile.close()

with open('DBLP_clean.csv', 'rb') as source:
    source_indices = dict((r[1],i) for i, r in enumerate(csv.reader(source)))           # create a dictionary map for titles and rows in the clean DBLP file
    
with open('DBLP_clean.csv', 'rb') as source:
    source_id = dict((i, r[0]) for i, r in enumerate(csv.reader(source)))               # create a dictionary map for DBLP IDs and rows in the clean DBLP file
    #print source_id

with open('Scholar_clean.csv', 'rb') as scholar:
    with open('DBLP_Scholar_perfectMapping_Mohamed.csv', 'wb') as results:              # Open the Scholar_clean file for comparison with DBLP_clean, and Open the converged File
        reader = csv.reader(scholar)
        writer = csv.writer(results)

        writer.writerow(["idDBLP", "idScholar", "DBLP_Match","Scholar_Match","Match_ID"]) # Define the first row for headers in the converged file
        next(reader)                                                                    # Skip first headers row
        for row in reader:
            index = source_indices.get(row[1])                                          # for each title in Scholar_clean, check existance in the Dict. Map for DBLP titles

            if index is not None:
                writer.writerow([source_id.get(index),row[0],str(index),row[5],str(index)+"_"+str(row[5])]) #If title is a match, write the information to the converged file
results.close()


