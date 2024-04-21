import pandas as pd

# Read the CSV file
df = pd.read_csv('states.csv')

# List of states you want to filter for
states_to_filter = ['India','Puducherry','Delhi','Goa', 'Chandigarh', 'Kerala','Bihar','Madhya Pradesh','Jharkhand','Uttar Pradesh','Odisha','Assam']  # Add your list of states here

# Filter the data for the states in the list
filtered_data = df[df['State'].isin(states_to_filter)]

# Save filtered data into separate CSV files for each state
for state in states_to_filter:
    state_data = filtered_data[filtered_data['State'] == state]
    state_data.to_csv(f'{state}.csv', index=False)
