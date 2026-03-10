import streamlit as st
import numpy as np
import pandas as pd
import growth_models as gm
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Microbial Growth Simulator",
    layout="wide",
)

# --- APP TITLE & DESCRIPTION ---
st.title("Microbial Growth Simulator")
st.markdown("""
Professional tool for modeling bacterial population dynamics. Simulate growth patterns 
using standard mathematical models and analyze the impact of environmental variables.
""")

# --- SIDEBAR: INPUT PARAMETERS ---
st.sidebar.header("Simulation Parameters")

model_choice = st.sidebar.selectbox(
    "Select Growth Model",
    ["Exponential Growth", "Logistic Growth"]
)

# Display the mathematical formula for the selected model
if model_choice == "Exponential Growth":
    st.latex(r"N(t) = N_0 e^{rt}")
else:
    st.latex(r"N(t) = \frac{K}{1 + \frac{K - N_0}{N_0} e^{-rt}}")

n0 = st.sidebar.number_input("Initial Population (N0)", min_value=1, value=100, step=10)
r = st.sidebar.slider("Intrinsic Growth Rate (r)", min_value=0.01, max_value=2.0, value=0.2, step=0.01)
time_duration = st.sidebar.number_input("Simulation Duration (hours)", min_value=1, value=24, step=1)

k = 0
if model_choice == "Logistic Growth":
    k = st.sidebar.number_input("Carrying Capacity (K)", min_value=10, value=5000, step=100)

st.sidebar.header("Environmental Variables")
temp = st.sidebar.slider("Temperature (Celsius)", min_value=0, max_value=100, value=37, step=1)
nutrients = st.sidebar.slider("Nutrient Availability (0.0 - 1.0)", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
antibiotics = st.sidebar.checkbox("Antibiotics Present")

# --- SIMULATION LOGIC ---
if st.button("Run Simulation"):
    with st.spinner("Processing..."):
        # Calculate modifiers for transparency
        import growth_models as gm
        modifier = gm.calculate_environmental_modifier(temp, nutrients, antibiotics)
        adjusted_r = r * modifier

        if model_choice == "Exponential Growth":
            time, pop = gm.exponential_growth(n0, r, int(time_duration), temp, nutrients, antibiotics)
        else:
            time, pop = gm.logistic_growth(n0, r, k, int(time_duration), temp, nutrients, antibiotics)

        # Create DataFrame for display and plots
        df = pd.DataFrame({
            "Time (hours)": time,
            "Population (N)": pop
        })

        # --- DISPLAY RESULTS ---
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Population Growth Analysis")
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(df["Time (hours)"], df["Population (N)"], marker='o', linestyle='-', color='#1f77b4', label=f"{model_choice}")
            ax.set_title(f"Microbial Population Dynamics ({model_choice})", fontsize=14)
            ax.set_xlabel("Time (hours)", fontsize=11)
            ax.set_ylabel("Bacterial Population (N)", fontsize=11)
            ax.grid(True, linestyle='--', alpha=0.6)
            ax.legend()
            st.pyplot(fig)

        with col2:
            st.subheader("Data Summary")
            st.dataframe(df, height=400)
            
            # --- CSV EXPORT ---
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Export Results to CSV",
                data=csv,
                file_name=f"microbial_growth_data_{model_choice.lower().replace(' ', '_')}.csv",
                mime='text/csv',
            )

        # --- SUMMARY METRICS ---
        st.subheader("Detailed Calculation Metrics")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Final Population", f"{pop[-1]:,.2f}")
        m2.metric("Input r", f"{r:.2f}")
        m3.metric("Adjusted r", f"{adjusted_r:.4f}")
        m4.metric("Env. Efficiency", f"{modifier*100:.1f}%")
        
        if adjusted_r != r:
            st.warning(f"Note: Environmental factors have adjusted your growth rate from {r:.2f} to {adjusted_r:.4f}.")

else:
    st.info("Please configure parameters in the sidebar and select 'Run Simulation' to generate results.")

# --- FOOTER ---
st.markdown("---")
st.markdown("Developed with Love by Srijon")
