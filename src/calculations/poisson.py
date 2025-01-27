import math

def calculate_poisson_probability(lmbda, k):
    result = (lmbda ** k * math.exp(-lmbda)) / math.factorial(k)
    steps = [
        f"P(X = {k}) = (λ^k * e^(-λ)) / k!",
        f"P(X = {k}) = ({lmbda}^{k} * e^(-{lmbda})) / {math.factorial(k)}",
        f"P(X = {k}) = {result}"
    ]
    return result, steps