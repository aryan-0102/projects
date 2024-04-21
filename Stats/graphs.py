import pandas as pd
import matplotlib.pyplot as plt

def plot_cumulative_data(file_names):
    # Create an empty DataFrame to store cumulative data
    cumulative_df = pd.DataFrame(columns=['Date', 'State', 'Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested'])
    
    # Iterate over each file name
    for file_name in file_names:
        # Read the CSV file
        df = pd.read_csv(file_name)
        
        # Calculate cumulative totals for each column
        df['Confirmed'] = df['Confirmed'].cumsum()
        df['Recovered'] = df['Recovered'].cumsum()
        df['Deceased'] = df['Deceased'].cumsum()
        df['Other'] = df['Other'].cumsum()
        df['Tested'] = df['Tested'].cumsum()
        
        # Append the data to the cumulative DataFrame
        cumulative_df = cumulative_df.append(df)
    
    # Plot the cumulative data
    plt.figure(figsize=(10, 6))
    for state in file_names:
        state_data = cumulative_df[cumulative_df['State'] == state[:-4]]  # Remove '.csv' from state name
        plt.plot(state_data['Date'], state_data['Confirmed'], label=state[:-4])  # Remove '.csv' from legend label
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.title('Cumulative Confirmed Cases')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# List of file names
file_names = ['India.csv', 'Puducherry.csv', 'Delhi.csv', 'Goa.csv', 'Chandigarh.csv', 'Kerala.csv']

# Call the function to plot the cumulative data
plot_cumulative_data(file_names)
