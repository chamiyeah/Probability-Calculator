def calculate_cross_probability(pmf_x, pmf_y, joint_pmf):
    """
    Calculate the conditional probability P(Y|X) and P(X|Y) based on the provided PMFs and joint PMF.
    
    Parameters:
    pmf_x (dict): Probability Mass Function of X.
    pmf_y (dict): Probability Mass Function of Y.
    joint_pmf (dict): Joint Probability Mass Function of X and Y.
    
    Returns:
    dict: Conditional probabilities P(Y|X) and P(X|Y).
    """
    conditional_p_y_given_x = {}
    conditional_p_x_given_y = {}

    # Calculate P(Y|X)
    for x in pmf_x:
        if pmf_x[x] > 0:
            conditional_p_y_given_x[x] = {y: joint_pmf.get((x, y), 0) / pmf_x[x] for y in pmf_y}

    # Calculate P(X|Y)
    for y in pmf_y:
        if pmf_y[y] > 0:
            conditional_p_x_given_y[y] = {x: joint_pmf.get((x, y), 0) / pmf_y[y] for x in pmf_x}

    return {
        "P(Y|X)": conditional_p_y_given_x,
        "P(X|Y)": conditional_p_x_given_y
    }