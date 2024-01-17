import pandas as pd

def parse_description(description, keys):
    """
    Revised function to parse the 'Description' column into multiple columns based on predefined keys.
    """
    parsed_data = {key: "" for key in keys}
    lines = description.split('\n')
    current_key = None

    for line in lines:
        # Check if the line contains any of the keys
        found_key = next((key for key in keys if line.startswith(key)), None)
        if found_key:
            current_key = found_key
            # Extract the value part of the line (after the key and potential colon)
            value = line[len(found_key):].lstrip(": ").strip()
            parsed_data[current_key] = value
        elif current_key:
            # Append line to the current key value
            parsed_data[current_key] += (' ' + line.strip()) if line.strip() else ''

    return parsed_data

# Load the CSV file
csv_file_path = 'dataset.csv'
df = pd.read_csv(csv_file_path)

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

# Apply the revised parsing function to the 'Description' column
parsed_columns = df['Description'].apply(lambda x: pd.Series(parse_description(x, keys)))

# Merge the new columns with the original DataFrame
df_expanded = df.join(parsed_columns)

# Save the expanded DataFrame to a new CSV file in the same directory
df_expanded.to_csv('expanded_dataset.csv', index=False)
