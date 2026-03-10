import numpy as np

def calculate_environmental_modifier(temperature, nutrient_availability, antibiotics_presence):
    """
    Calculate a growth rate modifier based on environmental factors.
    
    :param temperature: Current temperature (Celsius). Optimal 37°C for many bacteria.
    :param nutrient_availability: Factor from 0.0 to 1.0.
    :param antibiotics_presence: Boolean (True if present).
    :return: A scaling factor for the growth rate.
    """
    # Temperature effect (Optimal around 37°C, kills if too hot/cold)
    # Using a simple Gaussian-like curve for temperature impact
    opt_temp = 37
    temp_width = 15 # Standard deviation-like width
    temp_modifier = np.exp(-0.5 * ((temperature - opt_temp) / temp_width)**2)
    
    # Nutrient availability scales the growth rate linearly
    nutrient_modifier = nutrient_availability
    
    # Antibiotics reduce the growth rate (or even make it negative)
    antibiotic_modifier = 0.2 if antibiotics_presence else 1.0
    
    # Total modifier is the product of all factors
    return temp_modifier * nutrient_modifier * antibiotic_modifier

def exponential_growth(n0, r, time_steps, temp, nutrients, antibiotics):
    """
    Simulate exponential growth over time.
    Nt = N0 * e^(r*t)
    """
    modifier = calculate_environmental_modifier(temp, nutrients, antibiotics)
    adjusted_r = r * modifier
    
    time = np.arange(0, time_steps + 1)
    population = n0 * np.exp(adjusted_r * time)
    
    return time, population

def logistic_growth(n0, r, k, time_steps, temp, nutrients, antibiotics):
    """
    Simulate logistic growth over time using the analytical solution:
    Nt = K / (1 + ((K - N0) / N0) * e^(-r * t))
    
    This matches the continuous-time growth model (dN/dt = rN(1 - N/K)).
    """
    modifier = calculate_environmental_modifier(temp, nutrients, antibiotics)
    adjusted_r = r * modifier
    
    time = np.arange(0, time_steps + 1)
    
    # Analytical solution for Logistic Growth
    # N(t) = K / (1 + (K - n0)/n0 * exp(-adjusted_r * t))
    exponent_term = np.exp(-adjusted_r * time)
    denominator = 1 + ((k - n0) / n0) * exponent_term
    population = k / denominator
    
    return time, population
