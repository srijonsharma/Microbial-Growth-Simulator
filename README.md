# Microbial Growth Simulator

A Python-based simulation tool that models bacterial population growth over time using **Exponential** and **Logistic** growth models. The simulator considers environmental factors such as temperature, nutrient availability, and antibiotic presence to adjust growth rates dynamically.

## Features
- **Two Growth Models**:
  - **Exponential Growth**: Predicts population increase without constraints.
  - **Logistic Growth**: Incorporates a carrying capacity ($K$), where growth slows as it approaches resource limits.
- **Environmental Factors**:
  - **Temperature**: Adjusts growth based on an optimal range (around 37°C).
  - **Nutrient Availability**: Scales the growth rate based on resources.
  - **Antibiotic Presence**: Reduces the net growth rate significantly.
- **Visual Representation**: Generates a growth curve (Time vs. Population) using Matplotlib.
- **Data Export**: Exports simulation results to CSV for further analysis.
- **Interactive Interface**: Easy-to-use CLI for inputting simulation parameters.

## Project Structure
- `main.py`: Interactive entry point of the simulation.
- `growth_models.py`: Mathematical logic for population growth and environmental impacts.
- `visualization.py`: Handles graphical plotting and tabular data displays.
- `app.py`: Streamlit-based web application.

## Installation
Ensure you have Python installed, then install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage
### CLI Version
Run the simulation by executing:

```bash
python main.py
```

### Streamlit Web Version
To run the interactive web interface:

```bash
streamlit run app.py
```

Follow the prompts to:
1. Select a growth model and adjust parameters in the sidebar.
2. View real-time updates of the growth curve and data table.
3. Download simulation results as a CSV file.

## Deployment
This project is ready for deployment on **Streamlit Cloud**:
1. Upload the files to a GitHub repository.
2. Connect the repository to [Streamlit Cloud](https://streamlit.io/cloud).
3. Set the entry point to `app.py`.


The app is already deployed for use in the following URL:
```bash
https://microbial-growth-simulator.streamlit.app
```
