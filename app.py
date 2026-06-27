import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="PhytoDock Portal", layout="wide")

# 2. Title & Introduction
st.title("🌿 Molecular Docking Portal for Medicinal Plants")
st.markdown("""
Welcome to the interactive portal showcasing molecular docking studies of major bioactive compounds 
derived from traditional medicinal plants against therapeutic target proteins.
""")

# 3. Create Mock Data (Replace these values with your actual docking results!)
docking_data = {
    "Plant Source": ["Tulsi (Ocimum sanctum)", "Tulsi (Ocimum sanctum)", "Neem (Azadirachta indica)", "Neem (Azadirachta indica)", "Turmeric (Curcuma longa)"],
    "Phytochemical / Ligand": ["Eugenol", "Ursolic Acid", "Nimbin", "Azadirachtin", "Curcumin"],
    "Target Protein": ["Main Protease (Mpro)", "COX-2 Enzyme", "Main Protease (Mpro)", "Glycoprotein", "TNF-alpha"],
    "Binding Affinity (kcal/mol)": [-6.2, -8.4, -7.1, -9.3, -8.7],
    "Hydrogen Bonds": [2, 4, 1, 5, 3],
    "Status": ["Moderate Binding", "Strong Binding", "Moderate Binding", "Excellent Binding", "Strong Binding"]
}

df = pd.DataFrame(docking_data)

# 4. Interactive Sidebar Filters
st.sidebar.header("Filter Results")
selected_plant = st.sidebar.multiselect(
    "Select Medicinal Plant(s):",
    options=df["Plant Source"].unique(),
    default=df["Plant Source"].unique()
)

# Filter data based on selection
filtered_df = df[df["Plant Source"].isin(selected_plant)]

# 5. Dashboard Layout Split
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Docking Analysis Screening Data")
    st.dataframe(filtered_df, use_container_width=True)

with col2:
    st.subheader("💡 Key Insights")
    if not filtered_df.empty:
        best_binder = filtered_df.loc[filtered_df["Binding Affinity (kcal/mol)"].idxmin()]
        st.metric(
            label=f"Top Compound Selected", 
            value=best_binder["Phytochemical / Ligand"]
        )
        st.write(f"**Highest Affinity:** {best_binder['Binding Affinity (kcal/mol)']} kcal/mol against *{best_binder['Target Protein']}*.")
    else:
        st.write("Please select at least one plant in the sidebar.")

# 6. Documentation Section
st.markdown("---")
st.subheader("📚 Methodology Summary")
st.info("""
The molecular docking simulations presented here score binding configurations. 
A more negative binding affinity score (measured in **kcal/mol**) indicates a thermodynamically 
more stable and favorable interaction between the phytochemical ligand and the target protein receptor.
""")
