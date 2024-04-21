import pandas as pd
from scipy.stats import ttest_ind, f_oneway
import matplotlib.pyplot as plt

def perform_t_test(top_5_fatality_rates, rest_of_fatality_rates):
    """
    Perform a two-sample t-test to compare fatality rates between two groups.

    Args:
    top_5_fatality_rates (list): List of fatality rates for the top 5 HDI states.
    rest_of_fatality_rates (list): List of fatality rates for the rest of the states.

    Returns:
    tuple: t_statistic (float), p_value (float)
    """
    t_statistic, p_value = ttest_ind(top_5_fatality_rates, rest_of_fatality_rates)
    return t_statistic, p_value

def filter_and_calculate_fatality_rates(data_file, high_hdi_states, low_hdi_states):
    """
    Filter COVID-19 data for high and low HDI states, calculate fatality rates, and save them to CSV files.

    Args:
    data_file (str): Path to the CSV file containing COVID-19 data.
    high_hdi_states (list): List of high HDI states.
    low_hdi_states (list): List of low HDI states.

    Returns:
    pd.DataFrame: DataFrame containing all states' fatality rates.
    """
    # Read data
    data = pd.read_csv(data_file)

    # Filter data
    high_hdi_data = data[data['State'].isin(high_hdi_states)].copy()
    low_hdi_data = data[data['State'].isin(low_hdi_states)].copy()

    # Calculate fatality rates
    high_hdi_data.loc[:, 'Fatality Rate'] = (high_hdi_data['Deceased'] / high_hdi_data['Confirmed']) * 100
    low_hdi_data.loc[:, 'Fatality Rate'] = (low_hdi_data['Deceased'] / low_hdi_data['Confirmed']) * 100

    # Calculate fatality rate for India
    india_data = data[data['State'] == 'India'].copy()
    india_data.loc[:, 'Fatality Rate'] = (india_data['Deceased'] / india_data['Confirmed']) * 100

    # Save to CSV
    high_hdi_data[['State', 'Fatality Rate']].to_csv('highHDI.csv', index=False)
    low_hdi_data[['State', 'Fatality Rate']].to_csv('lowHDI.csv', index=False)
    india_data[['State', 'Fatality Rate']].to_csv('India.csv', index=False)

    # Combine data for all states
    all_states_data = pd.concat([high_hdi_data, low_hdi_data, india_data])

    # Save all states data to CSV
    all_states_data[['State', 'Fatality Rate']].to_csv('fatality.csv', index=False)

    return all_states_data


def plot_fatality_rates(data):
    """
    Plot fatality rates for high and low HDI states, and India's overall fatality rate.

    Args:
    data (pd.DataFrame): DataFrame containing fatality rates for all states.
    """
# National Fatality Rate
    india_data = data[data['State'] == 'India']
    india_fatality_rate = (india_data['Deceased'].sum() / india_data['Confirmed'].sum()) * 100

    # Calculate average fatality rate
    avg_fatality_rate_high_hdi = data[data['State'].isin(high_hdi_states)]['Fatality Rate'].mean()
    avg_fatality_rate_low_hdi = data[data['State'].isin(low_hdi_states)]['Fatality Rate'].mean()

    # Plotting
    plt.figure(figsize=(10, 6))

    # Bar plot for high HDI states
    plt.bar(data[data['State'].isin(high_hdi_states)]['State'], 
            data[data['State'].isin(high_hdi_states)]['Fatality Rate'], 
            color='blue', label='High HDI States')

    # Bar plot for low HDI states
    plt.bar(data[data['State'].isin(low_hdi_states)]['State'], 
            data[data['State'].isin(low_hdi_states)]['Fatality Rate'], 
            color='orange', label='Low HDI States')

    # Plot India's fatality rate
    plt.axhline(y=india_fatality_rate, color='red', linestyle='--', label='India Fatality Rate')

    # Plot average fatality rates
    plt.axhline(y=avg_fatality_rate_high_hdi, color='green', linestyle='--', label='Avg Fatality Rate (High HDI)')
    plt.axhline(y=avg_fatality_rate_low_hdi, color='purple', linestyle='--', label='Avg Fatality Rate (Low HDI)')

    plt.xticks(rotation=45)
    plt.ylabel('Fatality Rate (%)')
    plt.title('Fatality Rate Comparison')
    plt.legend()
    plt.tight_layout()
    plt.show()

def print_fatality_distribution(data):
    """
    Print the distribution of fatality rates.

    Args:
    data (pd.DataFrame): DataFrame containing fatality rates for all states.
    """
    

    # Plot histogram
    plt.figure(figsize=(8, 6))
    plt.hist(data['Fatality Rate'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Fatality Rate (%)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Fatality Rates')
    plt.grid(True)
    plt.show()

'''def main():
    # Filter and calculate fatality rates
    high_hdi_states = ['Kerala', 'Goa', 'Puducherry', 'Chandigarh', 'Delhi']
    low_hdi_states = ['Madhya Pradesh', 'Uttar Pradesh', 'Assam', 'Bihar', 'Odisha', 'Jharkhand']
    data = filter_and_calculate_fatality_rates('states.csv', high_hdi_states, low_hdi_states)

    # Fatality rates for the top 5 HDI states
    top_5_fatality_rates = data[data['State'].isin(high_hdi_states)]['Fatality Rate'].tolist()

    # Fatality rates for the rest of the states (excluding India)
    rest_of_fatality_rates = data[data['State'].isin(low_hdi_states)]['Fatality Rate'].tolist()

    # Perform two-sample t-test
    t_statistic, p_value_t_test = perform_t_test(top_5_fatality_rates, rest_of_fatality_rates)
    print("T-test:")
    print("T-statistic:", t_statistic)
    print("P-value:", p_value_t_test)

    # Perform ANOVA
    f_statistic, p_value_anova = f_oneway(top_5_fatality_rates, rest_of_fatality_rates)
    print("\nANOVA:")
    print("F-statistic:", f_statistic)
    print("P-value:", p_value_anova)

    # Print result
    if p_value_anova < 0.05:
        print("\nReject the null hypothesis. There is a significant difference in fatality rates among the groups.")
    else:
        print("\nAccept the null hypothesis. There is no significant difference in fatality rates among the groups.")

    # Plot fatality rates
    plot_fatality_rates

    '''
high_hdi_states = ['Kerala', 'Goa', 'Puducherry', 'Chandigarh', 'Delhi']
low_hdi_states = ['Madhya Pradesh', 'Uttar Pradesh', 'Assam', 'Bihar', 'Odisha', 'Jharkhand']
def main():
    # Filter and calculate fatality rates
    
    data = filter_and_calculate_fatality_rates('states.csv', high_hdi_states, low_hdi_states)

    # Fatality rates for the top 5 HDI states
    top_5_fatality_rates = data[data['State'].isin(high_hdi_states)]['Fatality Rate'].tolist()

    # Fatality rates for the rest of the states (excluding India)
    rest_of_fatality_rates = data[data['State'].isin(low_hdi_states)]['Fatality Rate'].tolist()

    # Perform two-sample t-test
    t_statistic, p_value_t_test = perform_t_test(top_5_fatality_rates, rest_of_fatality_rates)
    print("T-test:")
    print("T-statistic:", t_statistic)
    print("P-value:", p_value_t_test)

    # Perform ANOVA
    f_statistic, p_value_anova = f_oneway(top_5_fatality_rates, rest_of_fatality_rates)
    print("\nANOVA:")
    print("F-statistic:", f_statistic)
    print("P-value:", p_value_anova)

    # Print result
    if p_value_anova < 0.05:
        print("\nReject the null hypothesis. There is a significant difference in fatality rates among the groups.")
    else:
        print("\nAccept the null hypothesis. There is no significant difference in fatality rates among the groups.")

    # Plot fatality rates
    plot_fatality_rates(data)

    # Print fatality distribution
    

if __name__ == "__main__":
    main()
