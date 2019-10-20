import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Output", "budget_summary.txt")


total_months = 0
total_amount = 0

previous_rev = 0
revenue_diff = 0
greatest_incr = ["", 0]
greatest_decr = ["", 9999999999999999999999]

revenue_changes = []

with open(filepath) as bgt_data:
    csvreader = csv.DictReader(bgt_data)


    for row in csvreader:

        total_months = total_months + 1
        total_amount = total_amount + int(row["Profit/Losses"])



        revenue_diff = int(row["Profit/Losses"]) - previous_rev
        previous_rev = int(row["Profit/Losses"])
        #print (revenue_diff) 
        
        if (revenue_diff > greatest_incr[1]):
            greatest_incr = revenue_diff
            greatest_incr[0] = row["Date"]

        if (revenue_diff < greatest_decr[1]):
            greatest_decr[1] = revenue_diff
            greatest_decr[0] = row["Date"]

        revenue_changes.append(int(row["Profit/Losses"]))
        
    avg_changes= sum(revenue_changes) / len(revenue_changes)
    

    print("Total Months: " + str(total_months))
    print("Net Total amount: " + str(total_amount))
    print("Average Change: " + "$" + str(round(sum(revenue_diff) / len(revenue_diff),2)))
    print("Greatest Increase: " + " ($" +  str(greatest_incr[1]) + ")") 
    print("Greatest Decrease: " + " ($" +  str(greatest_decr[1]) + ")")

        


# Output Files
with open(output_file, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_amount))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_diff) / len(revenue_diff),2)))




