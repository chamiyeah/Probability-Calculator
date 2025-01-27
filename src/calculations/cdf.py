def calculate_cdf(pmf_values):
    """
    Calculate the Cumulative Distribution Function (CDF) from the given PMF values.
    
    Parameters:
    pmf_values (list): A list of probabilities representing the PMF.

    Returns:
    list: A list representing the CDF values.
    """
#     cdf_values = []
#     cumulative_sum = 0
#     for value in pmf_values:
#         cumulative_sum += value
#         cdf_values.append(cumulative_sum)
#     return cdf_values

# def detailed_cdf_calculation(pmf_values):
#     """
#     Provide a detailed step-by-step calculation of the CDF from PMF values.

#     Parameters:
#     pmf_values (list): A list of probabilities representing the PMF.

#     Returns:
#     str: A detailed explanation of the CDF calculation process.
#     """
#     steps = []
#     cumulative_sum = 0
#     for i, value in enumerate(pmf_values):
#         cumulative_sum += value
#         steps.append(f"Step {i + 1}: Add PMF value {value} to cumulative sum {cumulative_sum - value} = {cumulative_sum}")
#     return "\n".join(steps)
from scipy.integrate import quad

def calculate_cdf(distribution, a=None, b=None):
    steps = []
    if isinstance(distribution, dict):
        cumulative_sum = 0
        cdf_values = {}
        for x, p in sorted(distribution.items()):
            cumulative_sum += p
            cdf_values[x] = cumulative_sum
            steps.append(f"CDF Step: X = {x}, P(X) = {p}, Cumulative Sum = {cumulative_sum}")
        return cdf_values, steps
    else:
        # For continuous distribution, integrate the PDF
        def pdf(x):
            return eval(distribution.replace('x', str(x)))
        
        cdf_value, _ = quad(pdf, a, b)
        steps.append(f"Integral of PDF from {a} to {b} = {cdf_value}")
        return cdf_value, steps