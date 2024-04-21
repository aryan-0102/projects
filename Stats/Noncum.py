import pandas as pd
import matplotlib.pyplot as plt

def plot_non_cumulative_data(file_names):
    # Create an empty list to store DataFrames
    dfs = []
    
    # Iterate over each file name
    for file_name in file_names:
        # Read the CSV file
        df = pd.read_csv(file_name)
        
        # Create new columns for non-cumulative totals
        df['Non_Cumulative_Confirmed'] = df['Confirmed'] - df['Confirmed'].shift(1, fill_value=0)
        df['Non_Cumulative_Recovered'] = df['Recovered'] - df['Recovered'].shift(1, fill_value=0)
        df['Non_Cumulative_Deceased'] = df['Deceased'] - df['Deceased'].shift(1, fill_value=0)
        df['Non_Cumulative_Other'] = df['Other'] - df['Other'].shift(1, fill_value=0)
        df['Non_Cumulative_Tested'] = df['Tested'] - df['Tested'].shift(1, fill_value=0)
        
        # Append the DataFrame to the list
        dfs.append(df)
    
    # Concatenate all DataFrames into a single DataFrame
    non_cumulative_df = pd.concat(dfs, ignore_index=True)
    
    # Plot the non-cumulative data
    plt.figure(figsize=(10, 6))
    for state in file_names:
        state_data = non_cumulative_df[non_cumulative_df['State'] == state[:-4]]  # Remove '.csv' from state name
        plt.plot(state_data['Date'], state_data['Non_Cumulative_Confirmed'], label=state[:-4])  # Remove '.csv' from legend label
    plt.xlabel('Date')
    plt.ylabel('New Confirmed Cases')
    plt.title('Non-Cumulative New Confirmed Cases')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# List of file names
file_names = ['India.csv', 'Puducherry.csv', 'Delhi.csv', 'Goa.csv', 'Chandigarh.csv', 'Kerala.csv','Bihar.csv','Madhya Pradesh.csv','Jharkhand.csv','Uttar Pradesh.csv','Odisha.csv','Assam.csv']

# Call the function to plot the non-cumulative data
plot_non_cumulative_data(file_names)
