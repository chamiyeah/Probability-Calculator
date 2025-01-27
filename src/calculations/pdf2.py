from scipy.stats import norm

def calculate_pdf(mean, std_dev, x):
    result = norm.pdf(x, mean, std_dev)
    steps = [
        f"PDF(X = {x}) = P(X = {x})",
        f"Using the normal distribution with mean = {mean} and std_dev = {std_dev}",
        f"PDF(X = {x}) = {result}"
    ]
    return result, steps