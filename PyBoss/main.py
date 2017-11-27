import os, csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

new_header_list = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", 
"State"]

output_file = os.path.join("output_file_1.csv")

with open(output_file, "w", newline="") as datafile:
	writer = csv.writer(datafile)
	writer.writerow(new_header_list)

employee_csv = os.path.join("Resources", "employee_data1.csv")

with open(employee_csv, newline="") as csvfile:

	csvreader = csv.reader(csvfile, delimiter=",")

	for row in csvreader:
		if row[0] != "Emp ID":
			first_name = row[1].split(None, 1)[0]
			last_name = row[1].split(None, 2)[1]
			birth_date = row[2][5:7] + "/" + row[2][8:10] + "/" + row[2][0:4]
			ssn = "***-**-" + row[3][7:11]
			for key, value in us_state_abbrev.items():
				if row[4] == key:
					state = value
			row[1] = first_name
			row[2] = last_name
			row[3] = birth_date
			row[4] = ssn
			row.append(state)
			with open(output_file, "a", newline="") as datafile:
				writer = csv.writer(datafile)
				writer.writerows([row])
