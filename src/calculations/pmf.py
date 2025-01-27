def calculate_pmf(values):
    """
    Calculate the Probability Mass Function (PMF) for discrete random variables.
    
    Parameters:
    values (list): A list of values for which to calculate the PMF.
    
    Returns:
    dict: A dictionary with values as keys and their corresponding PMF as values.
    """
    total = sum(values)
    pmf = {value: value / total for value in values}
    return pmf

def detailed_pmf_calculation(values):
    """
    Provide a detailed step-by-step calculation of the PMF.
    
    Parameters:
    values (list): A list of values for which to calculate the PMF.
    
    Returns:
    str: A detailed explanation of the PMF calculation steps.
    """
    total = sum(values)
    steps = []
    steps.append(f"Total sum of values: {total}")
    
    for value in values:
        probability = value / total
        steps.append(f"PMF({value}) = {value} / {total} = {probability}")
    
    return "\n".join(steps)