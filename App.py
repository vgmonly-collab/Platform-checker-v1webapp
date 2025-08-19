import streamlit as st
import pandas as pd

# Rule set
rules = pd.DataFrame([
    {"Platform": "Amazon", "MaxBudget": 5000, "MaxMonths": 6},
    {"Platform": "Flipkart", "MaxBudget": 3000, "MaxMonths": 4},
    {"Platform": "Myntra", "MaxBudget": 2000, "MaxMonths": 3}
])

st.title("Platform Investment Checker")

# User inputs
platform = st.selectbox("Choose a platform", rules["Platform"])
budget = st.number_input("Enter your budget", min_value=0)
months = st.number_input("Enter number of months", min_value=1)

if st.button("Check"):
    rule = rules[rules["Platform"] == platform].iloc[0]
    
    if budget <= rule["MaxBudget"] and months <= rule["MaxMonths"]:
        result = "✅ Good"
    elif budget <= rule["MaxBudget"]*1.2 and months <= rule["MaxMonths"]*1.5:
        result = "⚠️ Reconsider"
    else:
        result = "❌ Big No"
    
    st.subheader(f"Result: {result}")
