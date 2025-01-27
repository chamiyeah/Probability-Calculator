#from scipy.integrate import quad

#def calculate_probability_range(pdf_function, a, b):
    # Define the PDF function
 #   def pdf(x):
  #      return eval(pdf_function.replace('x', str(x)))
    
    # Calculate the integral of the PDF from a to b
   # probability, _ = quad(pdf, a, b)
    #return probability


#from scipy.integrate import quad

#def calculate_probability_range(pdf_function, input_lower_bound, input_upper_bound):
 #   steps = []
    # Define the PDF function
  #  def pdf(x):
   #     return eval(pdf_function.replace('x', str(x)))
    
    # Calculate the integral of the PDF from input_lower_bound to input_upper_bound
   # probability, _ = quad(pdf, input_lower_bound, input_upper_bound)
   # steps.append(f"Integral of PDF from {input_lower_bound} to {input_upper_bound} = {probability}")
    
   # return probability, steps

from scipy.integrate import quad

def calculate_probability_range(pdf_function, input_lower_bound, input_upper_bound):
    steps = []
    # Define the PDF function
    def pdf(x):
        return eval(pdf_function.replace('x', str(x)))
    
    # Calculate the integral of the PDF from input_lower_bound to input_upper_bound
    probability, _ = quad(pdf, input_lower_bound, input_upper_bound)
    steps.append(f"Integral of PDF from {input_lower_bound} to {input_upper_bound} = {probability}")
    
    return probability, steps