def calculate_binomial_variance(n, p):
    steps = []
    variance = n * p * (1 - p)
    steps.append(f"Variance = n * p * (1 - p) = {n} * {p} * (1 - {p}) = {variance}")
    return variance, steps

def calculate_geometric_variance(p):
    steps = []
    variance = (1 - p) / (p ** 2)
    steps.append(f"Variance = (1 - p) / (p^2) = (1 - {p}) / ({p}^2) = {variance}")
    return variance, steps