import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(cur_path, '../data')
data_file = os.path.join(data_path, 'cohort_retention_data.csv')

# read data
data = pd.read_csv(data_file, parse_dates=['cohort_month'])
data['cohort_month'] = data['cohort_month'].dt.strftime('%Y-%m')
data = data.sort_values('cohort_month')


# Define the percentage formatter function
def percentage_formatter(x):

    return "{:.1f}%".format(x * 100)


# Pivot the synthetic data to create a matrix for the cohort pivot chart
cohort_pivot_chart_data = data.pivot(
    index='retention_day',
    columns='cohort_month',
    values='retention_rate'
)


# Apply the formatter to the pivot chart data
formatted_pivot_data = cohort_pivot_chart_data.applymap(percentage_formatter)

# Plot the cohort pivot chart using a heatmap
plt.figure(figsize=(14, 8))
plt.title('Cohort Pivot Chart')
sns.heatmap(cohort_pivot_chart_data, annot=formatted_pivot_data, cmap='BuPu', fmt="")
plt.xlabel('Install Month')
plt.ylabel('Retention Day')
plt.show()
