# # from math import comb

# # def calculate_binomial_probability(n, k, p):
# #     steps = []
# #     # Calculate binomial coefficient
# #     binomial_coefficient = comb(n, k)
# #     steps.append(f"Binomial Coefficient (n choose k) = {binomial_coefficient}")
    
# #     # Calculate probability
# #     probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
# #     steps.append(f"Probability P(X = {k}) = {binomial_coefficient} * ({p} ** {k}) * ((1 - {p}) ** ({n} - {k})) = {probability}")
    
# #     return probability, steps

from math import comb

def calculate_binomial_probability(n, k, p):
    steps = []
    # Calculate binomial coefficient
    binomial_coefficient = comb(n, k)
    steps.append(f"Binomial Coefficient (n choose k) = {binomial_coefficient}")
    
    # Calculate probability
    probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    steps.append(f"Probability P(X = {k}) = {binomial_coefficient} * ({p} ** {k}) * ((1 - {p}) ** ({n} - {k})) = {probability}")
    
    return probability, steps