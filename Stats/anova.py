from scipy.stats import ttest_ind

# Fatality rates for the top 5 HDI states
top_5_fatality_rates = [1.742643545, 1.254877955, 1.889017419, 1.451076, 0.6351722235]

# Fatality rates for the rest of the states (excluding India)
rest_of_fatality_rates = [0.8052120718, 1.327390097, 1.33906774, 1.473248976, 1.330554974]

# Perform two-sample t-test
t_statistic, p_value = ttest_ind(top_5_fatality_rates, rest_of_fatality_rates)

print("T-statistic:", t_statistic)
print("P-value:", p_value)
