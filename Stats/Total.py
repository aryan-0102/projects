import pandas as pd

def calculate_and_append_totals(file_names):
    for file_name in file_names:
        # Read the CSV file
        df = pd.read_csv(file_name)
        
        # Specify columns to calculate total for
        columns_to_sum = ['Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested']
        
        # Calculate the total for each specified column
        column_totals = df[columns_to_sum].sum()
        
        # Append the totals to the DataFrame
        totals_df = pd.DataFrame(column_totals).T
        
        # Write the totals to the CSV file
        with open(file_name, 'a') as f:
            totals_df.to_csv(f, mode='a', header=False, index=False)
            
# List of file names
file_names = ['India.csv','Puducherry.csv','Delhi.csv','Goa.csv', 'Chandigarh.csv', 'Kerala.csv','Bihar.csv','Madhya Pradesh.csv','Jharkhand.csv','Uttar Pradesh.csv','Odisha.csv','Assam.csv']  # Add your file names here

# Call the function with the list of file names
calculate_and_append_totals(file_names)
