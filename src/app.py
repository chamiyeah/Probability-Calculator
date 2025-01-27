import streamlit as st
from calculations.pdf2 import calculate_pdf
from calculations.cdf import calculate_cdf
from calculations.pmf import calculate_pmf
from calculations.variance import calculate_variance
from calculations.expected_value import calculate_expected_value
from calculations.cross_probability import calculate_cross_probability
from calculations.probability_range import calculate_probability_range
from calculations.binomial import calculate_binomial_probability
from calculations.distributions import calculate_binomial_variance, calculate_geometric_variance
from calculations.poisson import calculate_poisson_probability


def main():
    st.title("Probebility Calculator")
    st.sidebar.header("Input Parameters")

    distribution_type = st.sidebar.selectbox("Select Distribution Type", ["Discrete", "Continuous"])
    
    pmf_values = None
    pdf_function = None
    pmf_dict = None
    input_lower_bound = None
    input_upper_bound = None

    if distribution_type == "Discrete":
        pmf_values = st.sidebar.text_area("Enter PMF values (comma-separated, e.g., 0.2, 0.5, 0.3)", "0.2, 0.5, 0.3")
        pmf_values = list(map(float, pmf_values.split(','))) if pmf_values else None
        pmf_dict = {i + 1: pmf_values[i] for i in range(len(pmf_values))} if pmf_values else None
    else:
        pdf_function = st.sidebar.text_input("Enter PDF function (e.g., 3*x**2 / 2)")
        input_lower_bound = st.sidebar.number_input("Enter input lower bound a", value=0.0, format="%.2f")
        input_upper_bound = st.sidebar.number_input("Enter input upper bound b", value=1.0, format="%.2f")

    calculation_options = ["E(X)", "E(Y)", "CDF", "PDF", "Variance", "Cross Probability", "P(a <= X <= b)", "Binomial Probability", "Distribution Variance", "Poisson Probability"]
    selected_calculation = st.sidebar.selectbox("Choose Calculation", calculation_options)

    if selected_calculation == "E(Y)":
        y_function = st.sidebar.text_input("Enter Y as a function of X (e.g., X**2 - X)")

    if selected_calculation == "Binomial Probability":
        n = st.sidebar.number_input("Enter n (number of trials)", value=1, min_value=0)
        k = st.sidebar.number_input("Enter k (number of successes)", value=0, min_value=0)
        p = st.sidebar.number_input("Enter p (probability of success)", value=0.5, min_value=0.0, max_value=1.0, format="%.2f")

    if selected_calculation == "Distribution Variance":
        dist_type = st.sidebar.selectbox("Select Distribution", ["Binomial", "Geometric"])
        if dist_type == "Binomial":
            n = st.sidebar.number_input("Enter n (number of trials)", value=1, min_value=0)
            p = st.sidebar.number_input("Enter p (probability of success)", value=0.5, min_value=0.0, max_value=1.0, format="%.2f")
        elif dist_type == "Geometric":
            p = st.sidebar.number_input("Enter p (probability of success)", value=0.5, min_value=0.0, max_value=1.0, format="%.2f")

    if selected_calculation == "Poisson Probability":
        lmbda = st.sidebar.number_input("Enter λ (rate of occurrence)", value=1.0, format="%.2f")
        k = st.sidebar.number_input("Enter k (number of occurrences)", value=1, format="%d")
        result, steps = calculate_poisson_probability(lmbda, k)
        st.write(f"Poisson Probability P(X = {k}):", result)
        for step in steps:
            st.latex(step)
            
    if selected_calculation == "PDF":
        mean = st.sidebar.number_input("Enter mean (μ)", value=0.0, format="%.2f")
        std_dev = st.sidebar.number_input("Enter standard deviation (σ)", value=1.0, format="%.2f")
        x = st.sidebar.number_input("Enter value of X", value=0.0, format="%.2f")
        result, steps = calculate_pdf(mean, std_dev, x)
        st.write(f"PDF(X = {x}):", result)
        for step in steps:
            st.latex(step)

    if st.sidebar.button("Compute"):
        if selected_calculation == "E(X)":
            if pmf_values is not None:
                result, steps = calculate_expected_value(pmf_dict)
                st.write("Expected Value:", result)
                for step in steps:
                    st.write(step)
            elif pdf_function is not None:
                result, steps = calculate_expected_value(pdf_function, a=input_lower_bound, b=input_upper_bound)
                st.write("Expected Value:", result)
                for step in steps:
                    st.latex(step)
        elif selected_calculation == "E(Y)":
            if pmf_values is not None and y_function:
                result, steps = calculate_expected_value(pmf_dict, y_function)
                st.write("Expected Value of Y:", result)
                for step in steps:
                    st.write(step)
            elif pdf_function is not None and y_function:
                result, steps = calculate_expected_value(pdf_function, y_function, a=input_lower_bound, b=input_upper_bound)
                st.write("Expected Value of Y:", result)
                for step in steps:
                    st.latex(step)
        elif selected_calculation == "CDF":
            if pmf_values is not None:
                result, steps = calculate_cdf(pmf_dict)
                st.write("CDF:", result)
                for step in steps:
                    st.write(step)
            elif pdf_function is not None:
                result, steps = calculate_cdf(pdf_function, a=input_lower_bound, b=input_upper_bound)
                st.write("CDF:", result)
                for step in steps:
                    st.write(step)
        elif selected_calculation == "Variance":
            if pmf_values is not None:
                result, steps = calculate_variance(pmf_dict)
                st.write("Variance:", result)
                for step in steps:
                    st.write(step)
            elif pdf_function is not None:
                st.write("Variance calculation for continuous distribution is not implemented.")
        elif selected_calculation == "P(a <= X <= b)":
            if pdf_function:
                result, steps = calculate_probability_range(pdf_function, input_lower_bound, input_upper_bound)
                st.write("P(a <= X <= b):", result)
                for step in steps:
                    st.write(step)
        elif selected_calculation == "Binomial Probability":
            result, steps = calculate_binomial_probability(n, k, p)
            st.write(f"Binomial Probability P(X = {k}):", result)
            for step in steps:
                st.latex(step)
        elif selected_calculation == "Distribution Variance":
            if dist_type == "Binomial":
                result, steps = calculate_binomial_variance(n, p)
                st.write("Variance of Binomial Distribution:", result)
                for step in steps:
                    st.latex(step)
            elif dist_type == "Geometric":
                result, steps = calculate_geometric_variance(p)
                st.write("Variance of Geometric Distribution:", result)
                for step in steps:
                    st.latex(step)

if __name__ == "__main__":
    main()