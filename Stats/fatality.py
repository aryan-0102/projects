import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('states.csv')

# Filtering Data
high_hdi_states = ['Kerala', 'Goa', 'Puducherry', 'Chandigarh', 'Delhi']
low_hdi_states = ['Madhya Pradesh', 'Uttar Pradesh', 'Assam', 'Bihar', 'Odisha', 'Jharkhand']


high_hdi_data = data[data['State'].isin(high_hdi_states)].copy()
low_hdi_data = data[data['State'].isin(low_hdi_states)].copy()

# Calculate fatality rate 

high_hdi_data.loc[:, 'Fatality Rate'] = (high_hdi_data['Deceased'] / high_hdi_data['Confirmed']) * 100
low_hdi_data.loc[:, 'Fatality Rate'] = (low_hdi_data['Deceased'] / low_hdi_data['Confirmed']) * 100

# National Fatality Rate
india_data = data[data['State'] == 'India']
india_fatality_rate = (india_data['Deceased'].sum() / india_data['Confirmed'].sum()) * 100

# Calculate average fatality rate
avg_fatality_rate_high_hdi = high_hdi_data['Fatality Rate'].mean()
avg_fatality_rate_low_hdi = low_hdi_data['Fatality Rate'].mean()

# Plotting
plt.figure(figsize=(10, 6))

# Bar plot for high HDI states
plt.bar(high_hdi_data['State'], high_hdi_data['Fatality Rate'], color='blue', label='High HDI States')

# Bar plot for low HDI states
plt.bar(low_hdi_data['State'], low_hdi_data['Fatality Rate'], color='orange', label='Low HDI States')

# Plotting India's fatality rate
plt.axhline(y=india_fatality_rate, color='red', linestyle='--', label='India Fatality Rate')

# Plotting 
plt.axhline(y=avg_fatality_rate_high_hdi, color='green', linestyle='--', label='Avg Fatality Rate (High HDI)')
plt.axhline(y=avg_fatality_rate_low_hdi, color='purple', linestyle='--', label='Avg Fatality Rate (Low HDI)')

high_hdi_data[['State', 'Fatality Rate']].to_csv('highHDI.csv', index=False)
low_hdi_data[['State', 'Fatality Rate']].to_csv('lowHDI.csv', index=False)

# Combine data for all states
all_states_data = pd.concat([high_hdi_data, low_hdi_data])

# Saving into CSV file
all_states_data[['State', 'Fatality Rate']].to_csv('fatality.csv', index=False)


plt.xticks(rotation=45)
plt.ylabel('Fatality Rate (%)')
plt.title('Fatality Rate Comparison')
plt.legend()
plt.tight_layout()
plt.show()
