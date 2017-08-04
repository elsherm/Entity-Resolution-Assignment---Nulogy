# Entity-Resolution-Assignment---Nulogy
Entity Resolution Assignment developed in Python 

# The Assignment Instructions
The Code is developed using Python v2.7.13

Problem Description
“Entity resolution” is the problem of identifying which records in a database represent the
same entity. When dealing with user data, it is often difficult to control the quality of the
data inputted into the system. The poor quality of the data may be characterized by:
  • Duplicated records
  • Records that link to the same entity across different data sources
  • Data fields with more than one possible representation (e.g. “P&G” and “Procter and Gamble”)

Two datasets:
  1. Scholar.csv
  2. DBLP.csv

Each dataset contains the following columns:
Id[.csvName] title author venue year ROW_ID
There are records that reference the same entity across the two datasets.

# Bringing Everything Together
Your assignment is to resolve the records to their respective entities, and write a final
.csv named “DBLP_Scholar_perfectMapping_[YourName].csv” that only contain the
resolved entities. The final .csv file should include the following column headings:

 idDBLP: The matched DBLP.csv id
 idScholar: The matched Scholar.csv id
 DBLP_Match: The ROW_ID of the DBLP.csv file
 Scholar_Match: The ROW_ID of the Scholar.csv file
 Match_ID: A final column that combines the number from DBLP_Match and Scholar_Match, separated by an underscore.

The first row is provided as an example:
idDBLP            idScholar   DBLP_Match  Scholar_Match  Match_ID
conf/vldb/Levy96 lDTPyBMtHVwJ 1996        14            1996_14

# The Logic

1) Take DBLP1 as the source of truth
2) Remove any duplicates in the DBLP1 file by using Title, Author, Venue and Year as keys to identify duplicates
3) Remove all special characters found in the title field for both DBLP1 and Scholar, as these will be used as the Foriegn keys
4) Remove rows with Empty ScholarIDs in the Scholar.csv file, and log them in a file for intervention and inspection
5) Capitalize the titles in both files for better comparison
6) Hash the title field in the cleaned up DBLP file to compare with titles in the cleaned Scholar file.
7) Compare both cleaned up files based on Title. When a match is found store the DBLPID, ScholarID, DBLP Row ID, Scholar Row ID, and an appended column of both DBLP Row ID and Scholar RowID

# The code
The code is divided into 3 sections:
1) Cleaning up the Scholar file by removing rows with empty Scholar IDs, removing special characters from the titles, and capitalizing the titles
2) Cleaning up the DBLP1 file by removing duplicated, removing special characters from the titles, and capitalizing the titles
3) Creating dictionaries for the cleabed DBLP file for more efficient comparison with the cleaned Scholar file, and write the the output of the matched titles in a perfect mapped file, as outlined in the Bringing Everything Together section
