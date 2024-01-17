import pandas as pd

# Read the data from the file
with open('cell.txt', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.split('\n')

# Process each line to create a dictionary
data_dict = {}
for i in range(0, len(lines), 2):
    key = lines[i].strip()
    value = lines[i+1].strip() if i+1 < len(lines) else ''
    data_dict[key] = value

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame([data_dict])

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
