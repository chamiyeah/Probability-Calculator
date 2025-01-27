def calculate_pdf(x, mean, std_dev):
    import numpy as np
    from scipy.stats import norm

    # Step 1: Calculate the PDF using the normal distribution formula
    pdf_value = norm.pdf(x, mean, std_dev)

    # Step 2: Provide detailed calculations for students
    explanation = f"""
    To calculate the Probability Density Function (PDF) at x = {x}:
    1. We use the formula for the normal distribution:
       PDF(x) = (1 / (σ * √(2π))) * e^(-((x - μ)² / (2σ²)))
    2. Where:
       - μ (mean) = {mean}
       - σ (standard deviation) = {std_dev}
    3. Substituting the values into the formula gives us:
       PDF({x}) = {pdf_value}
    """

    return pdf_value, explanation

def calculate_pdf_array(x_values, mean, std_dev):
    pdf_values = [calculate_pdf(x, mean, std_dev)[0] for x in x_values]
    return pdf_values