import pandas as pd

# Load the 'Separated US Express Rates' workbook
rates_xls = pd.ExcelFile('path/to/Separated US Express Rates.xlsx')

# Load the 'DMG Automation Sample Files' (Charges) workbook
charges_df = pd.read_excel('path/to/DMG Automation Sample Files.xlsx')

# Function to retrieve the rate from the rate sheet
def get_rate(rate_sheet, weight, zone):
    # Assuming the first column is weight and the first row contains zone headers
    if weight in rate_sheet.index and zone in rate_sheet.columns:
        return rate_sheet.at[weight, zone]
    else:
        return None

# Function to calculate price for a row in the charges dataframe
def calculate_price(row):
    service_type = row['Service Type']
    weight = row['RW']
    zone = row['Z']

    # Check if the service type has a corresponding rate sheet
    if service_type in rates_xls.sheet_names:
        rate_sheet_df = rates_xls.parse(service_type, index_col=0)
        
        # Retrieve the rate
        rate = get_rate(rate_sheet_df, weight, zone)

        # Multiply by total items or weight if it's a multi-weight or freight shipment
        if service_type.startswith('MW'):
            total_items = row.get('Total Pieces', 1)  # Replace 'Total Pieces' with the actual column name if different
            return rate * total_items if rate is not None else None
        elif service_type.endswith('Freight'):
            return rate * weight if rate is not None else None 
        else:
            return rate
    else:
        # No rate sheet for this service type
        return None

# Apply the calculate_price function to each row in the charges dataframe
charges_df['Calculated Price'] = charges_df.apply(calculate_price, axis=1)

# Write the updated dataframe back to a new Excel file
charges_df.to_excel('path/to/Updated DMG Automation Sample Files.xlsx', index=False)
