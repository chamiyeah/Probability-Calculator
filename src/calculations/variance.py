def calculate_variance(distribution):
    steps = []
    if isinstance(distribution, dict):
        # Calculate E(X)
        expected_value = sum(x * p for x, p in distribution.items())
        steps.append(f"E(X) = {expected_value}")
        
        # Calculate E(X^2)
        expected_value_squared = sum((x ** 2) * p for x, p in distribution.items())
        steps.append(f"E(X^2) = {expected_value_squared}")
        
        # Calculate Variance
        variance = expected_value_squared - (expected_value ** 2)
        steps.append(f"Variance = E(X^2) - [E(X)]^2 = {expected_value_squared} - ({expected_value}^2) = {variance}")
    else:
        # For continuous distribution, you would need to integrate
        variance = None
        steps.append("Variance calculation for continuous distribution is not implemented.")
    
    return variance, steps