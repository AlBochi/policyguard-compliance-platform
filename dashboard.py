import streamlit as st
import json
import pandas as pd

# Load violations
try:
    with open("violations.json") as f:
        raw_data = json.load(f)
    violations = raw_data.get("result", [])[0].get("expressions", [])[0].get("value", [])
except Exception as e:
    violations = []
    st.error(f"Error loading violations: {e}")

# Title
st.set_page_config(page_title="PolicyGuard Compliance Dashboard", layout="wide")
st.title("📊 PolicyGuard Compliance Dashboard")

# Display
if violations:
    st.subheader("🚨 Active Violations")
    df = pd.DataFrame(violations, columns=["Violation"])
    st.dataframe(df, use_container_width=True)
    st.metric("Violations Found", len(violations))
else:
    st.success("✅ No active violations found.")
