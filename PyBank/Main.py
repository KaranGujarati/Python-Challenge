import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Output", "budget_summary.txt")

#total_months = []
#total_amount = []
#total_amount = list(map(int, total_amount))

total_months = 0
total_amount = 0

revenue_changes = []

with open(file_to_load) as bgt_data:
    csvreader = csv.DictReader(bgt_data)


    for row in csvreader:

        total_months = total_months + 1
        total_amount = total_amount + int(row["Profit/Losses"])

        revenue_changes.append(int(row["Profit/Losses"]))
        
    avg_changes= sum(revenue_changes) / len(revenue_changes)
    #avg_changes= total_amount / total_months


    print("Total Months: " + str(total_months))
    print("Net Total amount: " + str(total_amount))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))

        
  #      total_months = total_months + [row[0]]

 #       total_amount = total_amount + [row[1]]
        

#print ("The total number of months : " + str(len(total_months)))

#print ("The net total amount over the entire period : ", str(total_amount))
#print (total_amount)

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))





