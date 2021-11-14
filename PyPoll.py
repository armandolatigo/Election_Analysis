#  The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote



#import modules
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data. 
    file_reader = csv.reader(election_data)
# Print each row in the CSV file
    headers = next(file_reader)
    print(headers)
    
    
    #for row in file_reader:
     #   print(row)










#Using the open() function with the "w" mode we will write data to the file
#    txt_file = open(file_to_save, "w")
#Write three counties to the file
 #   txt_file.write("------------------------\n")
 #   txt_file.write("Araphoe\n")
 #   txt_file.write("Denver\n")
 #   txt_file.write("Jefferson\n")
#Close the file
  #  txt_file.close()

