
import os, csv, math

totalmonths = 0
totalrevenue = 0
revchange = 0
priorrevchange = 0
totalrevchange = 0
greatincrease = 0
greatdecrease = 0
previous = ['Date','Revenue']

budget_csv = os.path.join("Resources", "budget_data_1.csv")




with open(budget_csv, newline="") as csvfile:

	csvreader = csv.reader(csvfile, delimiter=",")


	for row in csvreader:
		if row[0] != 'Date':
			totalmonths = totalmonths + 1
			totalrevenue = totalrevenue + int(row[1])
		if previous[0]	!= 'Date':
			revchange = int(row[1]) - int(previous[1])
			if revchange > greatincrease:
				greatincrease = revchange
				increasemonth = row[0]
			elif revchange < greatdecrease:
				greatdecrease = revchange
				decreasemonth = row[0]
			totalrevchange = totalrevchange + revchange
			priorrevchange = revchange
		previous = row
	averagerevchange = totalrevchange / (totalmonths - 1)
	print("\n")
	print("Financial Analysis")
	print("----------------------------")
	print("Total Months: " + str(totalmonths))
	print("Total Revenue: $" + str(totalrevenue))
	print("Average Revenue Change: $" + str(math.floor(averagerevchange)))
	print("Greatest Increase in Revenue: " + increasemonth + " ($" + str(greatincrease) + ")")
	print("Greatest Decrease in Revenue: " + decreasemonth + " ($" + str(greatdecrease) + ")")

output_file = os.path.join("output_file_1.txt")

with open(output_file, "w", newline="") as datafile:
	writer = csv.writer(datafile)
	writer.writerow(["Financial Analysis"])
	writer.writerow(["----------------------------"])
	writer.writerow(["Total Months: " + str(totalmonths)])
	writer.writerow(["Total Revenue: $" + str(totalrevenue)])
	writer.writerow(["Average Revenue Change: $" + str(math.floor(averagerevchange))])
	writer.writerow(["Greatest Increase in Revenue: " + increasemonth + " ($" + str(greatincrease) + ")"])
	writer.writerow(["Greatest Decrease in Revenue: " + decreasemonth + " ($" + str(greatdecrease) + ")"])