#def calculate_expected_value(pmf_values=None, pdf_values=None):
#    if pmf_values is not None:
       # expected_value = sum(x * p for x, p in pmf_values.items())
      #  steps = [f"E(X) = Σ [x * P(X=x)] = {expected_value}"]
     #   return expected_value, steps
    #elif pdf_values is not None:
   #     expected_value = sum(x * p for x, p in pdf_values.items())
   #     steps = [f"E(X) = ∫ [x * f(x) dx] = {expected_value}"]
  #      return expected_value, steps
 #   else:
#        return None, ["No values provided for calculation."]
    
    
# from scipy.integrate import quad

# def calculate_expected_value(distribution, y_function=None, a=None, b=None):
#     steps = []
#     if isinstance(distribution, dict):
#         if y_function:
#             # Calculate E(Y) where Y is a function of X
#             expected_value = 0
#             for x, p in distribution.items():
#                 y = eval(y_function.replace('X', str(x)))
#                 steps.append(f"E(Y) Step: Y = {y}, P(X) = {p}, Contribution = {y * p}")
#                 expected_value += y * p
#         else:
#             # Calculate E(X)
#             expected_value = 0
#             for x, p in distribution.items():
#                 steps.append(f"E(X) Step: X = {x}, P(X) = {p}, Contribution = {x * p}")
#                 expected_value += x * p
#     else:
#         # For continuous distribution, integrate the PDF
#         def pdf(x):
#             return eval(distribution.replace('x', str(x)))
        
#         if y_function:
#             def y_pdf(x):
#                 y = eval(y_function.replace('X', str(x)))
#                 return y * pdf(x)
            
#             expected_value, _ = quad(y_pdf, a, b)
#             steps.append(f"Integral of Y*PDF from {a} to {b} = {expected_value}")
#         else:
#             expected_value, _ = quad(lambda x: x * pdf(x), a, b)
#             steps.append(f"Integral of X*PDF from {a} to {b} = {expected_value}")
    
#     return expected_value, steps

from scipy.integrate import quad

def calculate_expected_value(distribution, y_function=None, a=None, b=None):
    steps = []
    if isinstance(distribution, dict):
        if y_function:
            # Calculate E(Y) where Y is a function of X
            expected_value = 0
            for x, p in distribution.items():
                y = eval(y_function.replace('X', str(x)))
                steps.append(f"E(Y) Step: Y = {y}, P(X) = {p}, Contribution = {y * p}")
                expected_value += y * p
        else:
            # Calculate E(X)
            expected_value = 0
            for x, p in distribution.items():
                steps.append(f"E(X) Step: X = {x}, P(X) = {p}, Contribution = {x * p}")
                expected_value += x * p
    else:
        # For continuous distribution, integrate the PDF
        def pdf(x):
            return eval(distribution.replace('x', str(x)))
        
        if y_function:
            def y_pdf(x):
                y = eval(y_function.replace('X', str(x)))
                return y * pdf(x)
            
            expected_value, _ = quad(y_pdf, a, b)
            steps.append(f"Integral of Y*PDF from {a} to {b} = {expected_value}")
        else:
            expected_value, _ = quad(lambda x: x * pdf(x), a, b)
            steps.append(f"Integral of X*PDF from {a} to {b} = {expected_value}")
    
    return expected_value, steps