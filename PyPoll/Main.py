import os
import csv
from collections import OrderedDict
from operator import itemgetter

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Output", "election_results.txt")

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}


with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    
    
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")


    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#election results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")



# Output 
with open(file_to_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))