import pandas as pd

# List of predefined keys
keys = [
    "Sales Rep",
    "Quote Type",
    "Customer Business Name",
    "Customer Contact Name",
    "Customer Contact E-mail Address",
    "Customer Contact Phone Number",
    "Customer Address",
    "Cross Selling Opportunity",
    "Cross Sales Business Unit",
    "Vendor Discount Required",
    "Finders Fee to be Applied - Please indicate Name for Remittance or N.A.",
    "Industry Sector",
    "Description of Customer's Needs",
    "Spare Parts Package",
    "Customer Expected Project Completion Date",
    "Drawings Required?",
    "Installation Required?",
    "Installation Pricing is (Select)",
    "File Attachments"
]

def process_block_with_defined_keys(block, keys):
    """
    Process a single block of text using predefined keys.
    """
    lines = block.strip().split('\n')
    record = {key: "" for key in keys}
    current_key = None

    for line in lines:
        # Check if the line is a key
        if line in keys:
            current_key = line
        elif current_key:
            # Append line to the current key value
            record[current_key] += line.strip() + ' '
    
    # Trim trailing spaces from values
    for key in record:
        record[key] = record[key].strip()

    return record

# Path to the text file
text_file_path = 'cell.txt'

# Read the data from the file
with open(text_file_path, 'r') as file:
    data = file.read()

# Split the data into blocks, using ';;;' as the delimiter
blocks = data.split(';;;')

# Process each block using the predefined keys
records = [process_block_with_defined_keys(block, keys) for block in blocks if block.strip()]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(records)

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
