import matplotlib.pyplot as plt
import csv

def plot_growth_curve(time_data, population_data, model_type):
    """
    Plot Time vs Population using Matplotlib.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time_data, population_data, marker='o', linestyle='-', color='b', label=f"{model_type} Growth")
    plt.title(f"Microbial Population Growth ({model_type} Model)")
    plt.xlabel("Time (hours)")
    plt.ylabel("Bacterial Population (N)")
    plt.grid(True)
    plt.legend()
    plt.show()

def display_results_table(time_data, population_data):
    """
    Print a formatted table showing Time vs Population.
    """
    print(f"{'Time (hrs)':<12} | {'Population (N)':<15}")
    print("-" * 30)
    for t, p in zip(time_data, population_data):
        print(f"{t:<12} | {p:<15.2f}")

def export_to_csv(time_data, population_data, filename="simulation_results.csv"):
    """
    Export simulation data to a CSV file.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time (hours)", "Population (N)"])
        for t, p in zip(time_data, population_data):
            writer.writerow([t, p])
    print(f"Data exported successfully to {filename}.")
