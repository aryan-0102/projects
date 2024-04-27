# COVID-19 Fatality Analysis

This Python script analyzes fatality rates of COVID-19 across different states based on their Human Development Index (HDI). It performs statistical tests to compare fatality rates between states with high HDI and those with low HDI, and also provides visualizations to aid in understanding the distribution and comparison of fatality rates.

## Dependencies

Ensure you have the following Python libraries installed:

- pandas
- scipy
- matplotlib

You can install them using pip:

```python3
pip install pandas scipy matplotlib
```


## Usage

1. **Clone the Repository:**

   Clone this repository to your local machine:

```python3
git clone https://github.com/aryan-0102/stats.git
```

2. **Run the Script:**

Navigate to the directory containing the script and run it using Python:

```python3
python main.py
```


3. **Input Data:**

Ensure you have the COVID-19 data in CSV format. The script expects a CSV file named `states.csv` containing the following columns:

- State
- Confirmed
- Deceased

4. **Output Files:**

After running the script, it will generate the following output files:

- `highHDI.csv`: Fatality rates for states with high HDI.
- `lowHDI.csv`: Fatality rates for states with low HDI.
- `India.csv`: Fatality rates for India.
- `fatality.csv`: Fatality rates for all states combined.

## Functions

- `perform_t_test`: Performs a two-sample t-test to compare fatality rates between two groups.
- `filter_and_calculate_fatality_rates`: Filters COVID-19 data for high and low HDI states, calculates fatality rates, and saves them to CSV files.
- `plot_fatality_rates`: Plots fatality rates for high and low HDI states, and India's overall fatality rate.
- `print_fatality_distribution`: Prints the distribution of fatality rates.

## Example

```python
import pandas as pd
from fatality_analysis import main

# Define high HDI states and low HDI states
high_hdi_states = ['Kerala', 'Goa', 'Puducherry', 'Chandigarh', 'Delhi']
low_hdi_states = ['Madhya Pradesh', 'Uttar Pradesh', 'Assam', 'Bihar', 'Odisha', 'Jharkhand']

# Run the analysis
main()
```

