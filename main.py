import growth_models as gm
import visualization as viz
import numpy as np

def get_float_input(prompt, default=None):
    """
    Helper function for input validation.
    """
    while True:
        user_input = input(f"{prompt} {'(default: ' + str(default) + ')' if default is not None else ''}: ")
        if not user_input and default is not None:
            return default
        try:
            val = float(user_input)
            if val < 0:
                print("Error: Input cannot be negative.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid numerical value.")

def main():
    print("=" * 60)
    print("Welcome to the Microbial Growth Simulator!")
    print("=" * 60)

    # 1. Choose Growth Model
    print("\nSelect Growth Model:")
    print("1. Exponential Growth Model")
    print("2. Logistic Growth Model")
    choice = input("Choice (1/2): ")

    # 2. Gather User Parameters
    n0 = get_float_input("Initial bacterial population (N0)", 100)
    r = get_float_input("Intrinsic growth rate (r, e.g., 0.1 for 10% growth per hour)", 0.2)
    time_steps = int(get_float_input("Duration of simulation (hours)", 24))
    
    k = 0
    if choice == '2':
        k = get_float_input("Carrying capacity (K)", 5000)

    # 3. Gather Environmental Factors
    print("\nEnvironmental Factors:")
    temperature = get_float_input("Temperature (Celsius, 37 is optimal)", 37)
    nutrients = get_float_input("Nutrient availability (0 to 1, where 1 is abundance)", 1.0)
    antibiotics = input("Is antibiotic present? (y/n): ").lower() == 'y'

    # 4. Perform Simulation
    print("\nSimulating growth...")
    if choice == '1':
        time, pop = gm.exponential_growth(n0, r, time_steps, temperature, nutrients, antibiotics)
        model_name = "Exponential"
    else:
        time, pop = gm.logistic_growth(n0, r, k, time_steps, temperature, nutrients, antibiotics)
        model_name = "Logistic"

    # 5. Display Results
    print("\nSimulation results:")
    viz.display_results_table(time, pop)
    
    # 6. Export data
    export_choice = input("\nExport results to CSV? (y/n): ").lower()
    if export_choice == 'y':
        filename = f"microbial_growth_{model_name.lower()}_simulation.csv"
        viz.export_to_csv(time, pop, filename)

    # 7. Visualize results
    print("\nGenerating growth curve plot...")
    viz.plot_growth_curve(time, pop, model_name)

if __name__ == "__main__":
    main()
