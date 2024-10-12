import numpy as np
import pandas as pd
from statsmodels.stats.power import NormalIndPower, proportion_effectsize
from scipy.stats import chi2_contingency

# Step 1: Compute the required sample size for the test

# Parameters
alpha = 0.05  # 95% confidence interval, so alpha is 0.05
power = 0.80  # 80% power
baseline_conversion_rate = 0.12  # Baseline conversion rate (button color: blue)
min_detectable_effect = 0.03  # Minimum detectable difference (change from blue to red)

# Calculate the effect size
effect_size = proportion_effectsize(
    baseline_conversion_rate, baseline_conversion_rate + min_detectable_effect
)

# Initialize the power analysis
analysis = NormalIndPower()

# Compute required sample size per group
sample_size_per_group = analysis.solve_power(
    effect_size=effect_size, alpha=alpha, power=power, alternative="two-sided"
)
sample_size_per_group = int(
    np.ceil(sample_size_per_group)
)  # Round up to nearest whole number

print(f"Required sample size per group: {sample_size_per_group}")

# Step 2: Generate random A/B test data (Group A: blue button, Group B: red button)

# Set random seed for reproducibility
np.random.seed(42)

# Generate data for Group A (blue button)
conversion_rate_A = baseline_conversion_rate  # 12% conversion rate
group_A = pd.DataFrame(
    {
        "group": "A",
        "user_id": range(1, sample_size_per_group + 1),
        "converted": np.random.binomial(1, conversion_rate_A, sample_size_per_group),
    }
)

# Generate data for Group B (red button)
conversion_rate_B = (
    baseline_conversion_rate + min_detectable_effect
)  # 12% + 3% = 15% conversion rate
group_B = pd.DataFrame(
    {
        "group": "B",
        "user_id": range(1, sample_size_per_group + 1),
        "converted": np.random.binomial(1, conversion_rate_B, sample_size_per_group),
    }
)

# Combine both groups
ab_test_data = pd.concat([group_A, group_B], ignore_index=True)

# Step 3: Perform the A/B test by calculating rates and conducting hypothesis test

# Calculate conversion rates
conversion_A = group_A["converted"].mean()
conversion_B = group_B["converted"].mean()

# Perform a chi-square test to determine if there is a statistically significant difference
contingency_table = pd.crosstab(ab_test_data["group"], ab_test_data["converted"])
chi2, p_value, _, _ = chi2_contingency(contingency_table)


# Step 4: Interpret the A/B test result and provide a recommendation
def interpret_ab_test(conversion_A, conversion_B, p_value, alpha=0.05):
    print(f"Conversion rate for Group A (blue button): {conversion_A:.2%}")
    print(f"Conversion rate for Group B (red button): {conversion_B:.2%}")
    print(f"P-value: {p_value:.5f}")

    if p_value < alpha:
        print(f"Since the p-value is less than {alpha}, we reject the null hypothesis.")
        print(
            "There is a statistically significant difference between Group A and Group B."
        )
        if conversion_B > conversion_A:
            print(
                "Recommendation: The red button performs better. Consider switching to the red button."
            )
        else:
            print(
                "Recommendation: The blue button performs better. Consider keeping the blue button."
            )
    else:
        print(
            f"Since the p-value is greater than {alpha}, we fail to reject the null hypothesis."
        )
        print(
            "There is no statistically significant difference between Group A and Group B."
        )
        print("Recommendation: No change should be made based on these results.")


# Step 5: Use a 95% confidence interval for decision making

# Interpret and provide recommendation
interpret_ab_test(conversion_A, conversion_B, p_value)
