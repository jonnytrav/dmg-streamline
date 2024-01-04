# import pandas as pd
import xlwings as xw

def read_from_cell():
    # Open the workbook and sheet
    wb = xw.Book('../../../TESTINGPYTHON.xlsx')
    sheet = wb.sheets['SmokeTest']

    # Read value from a specific cell
    value = sheet.range('A1').value  # Using Excel cell address
    # Or using row and column index (indexing starts at 1)
    # value = sheet.range(1, 1).value
    print(value)

    wb.close()  # Close the workbook
    # return value

# def write_to_cell(value):
#     # Open the workbook and sheet
#     wb = xw.Book('path/to/your/excel/file.xlsx')
#     sheet = wb.sheets['Sheet1']  # Replace with your sheet name

#     # Write value to a specific cell
#     sheet.range('A1').value = value  # Using Excel cell address
#     # Or using row and column index
#     # sheet.range(1, 1).value = value

#     wb.save()  # Save the workbook
#     wb.close()  # Close the workbook



# ********BELOW UTILIZES PANDAS, BUT XLWINGS IS MORE VERBOSE*****************************

# def process_excel(file_path):
#     # Load the Excel file
#     df = pd.read_excel(file_path)

#     # Your processing logic here
#     # For example, df['New Column'] = df['Existing Column'] * 10

#     # Return the processed DataFrame
#     return df

# if __name__ == "__main__":
#     # Example file path - replace with your actual file path
#     file_path = 'path/to/your/excel/file.xlsx'
#     processed_df = process_excel(file_path)
    
#     # Save the processed DataFrame to a new Excel file
#     processed_df.to_excel('path/to/your/processed_file.xlsx', index=False)
