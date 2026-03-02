import streamlit as st
import pandas as pd


def render():

    # 🔥 Section-specific CSS (safe + clean)
    st.markdown("""
    <style>

    /* Control catalog container */
    .control-card {
        background-color: #ffffff;
        color: #000000;
        padding: 15px;
        border-radius: 10px;
    }

    /* Expander header text */
    div[data-testid="stExpander"] summary {
        color: #000000 !important;
        font-weight: 600;
    }

    /* Expander body */
    div[data-testid="stExpanderDetails"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* Paragraph text inside expander */
    div[data-testid="stExpanderDetails"] p {
        color: #000000 !important;
    }

    /* 🔥 Fix dropdown text color */
    div[data-baseweb="select"] * {
        color: black !important;
    }

    div[data-baseweb="popover"] * {
        color: black !important;
        background-color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 📚 India AI Governance – Control Catalog")

    # Load Excel
    df = pd.read_excel(
        "data/India_AI_Governance_Framework_Playbook_FINAL_DETAILED.xlsx",
        engine="openpyxl"
    )

    # Filters
    col1, col2 = st.columns(2)

    with col1:
        stage_filter = st.selectbox(
            "Filter by Lifecycle Stage",
            ["All"] + sorted(df["Lifecycle Stage"].unique())
        )

    with col2:
        risk_filter = st.selectbox(
            "Filter by Risk Level",
            ["All"] + sorted(df["Applicable Risk Level"].unique())
        )

    search = st.text_input("🔍 Search Control Title")

    # Apply filters
    filtered_df = df.copy()

    if stage_filter != "All":
        filtered_df = filtered_df[
            filtered_df["Lifecycle Stage"] == stage_filter
        ]

    if risk_filter != "All":
        filtered_df = filtered_df[
            filtered_df["Applicable Risk Level"] == risk_filter
        ]

    if search:
        filtered_df = filtered_df[
            filtered_df["Control Title"].str.contains(search, case=False)
        ]

    st.markdown(f"### Showing {len(filtered_df)} Controls")

    # Display controls
for _, row in filtered_df.iterrows():
    with st.expander(f"{row['Control ID']} — {row['Control Title']}"):

        st.write("**Lifecycle Stage:**", row["Lifecycle Stage"])
        st.write("**Category:**", row["Control Category"])
        st.write("**Risk Level:**", row["Applicable Risk Level"])
        st.write("**Responsible Role:**", row["Responsible Role"])

        st.markdown("### Control Description")
        st.write(row["Detailed Control Description (~150 words)"])

        st.markdown("### Regulatory Mapping")
        st.write(row["Detailed Regulatory Mapping"])

        st.markdown("### References")
        st.markdown("- [DPDP Act 2023](https://www.meity.gov.in/writereaddata/files/DPDP%20Act%202023.pdf)")
        st.markdown("- [CERT-In Directions](https://www.cert-in.org.in/)")
        st.markdown("- [ISO 42001](https://www.iso.org/standard/81230.html)")
