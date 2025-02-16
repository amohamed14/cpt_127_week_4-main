
'''

This assignment is supposed to  read in the CSV
file and calculate an average grade for the class.

Please find the error and fix it!

You will know the problem is solved when you get an output of:

The average grade for the class is: 84.75

'''


#%%

# Open the CSV file in read mode
with open('student_grades.csv', 'r') as f:
    # Collect all lines from the file
    lines = f.readlines()

    # Validate file has data
    if len(lines) > 1:  # Ensure there's more than just the header
        grades = []

        # Iterate through each line and collect the grade, skipping the first 'header' line
        for line in lines[1:]:
            # Split the line into a list (i.e., columns)
            row = line.strip().split(',')

            # Convert the grade to a float and add it to the list
            grades.append(float(row[3]))

        # Calculate the average
        avg = sum(grades) / len(grades)

        print(f'The average grade for the class is: {avg}')



