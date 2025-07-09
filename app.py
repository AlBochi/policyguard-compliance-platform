import streamlit as st
import pandas as pd
import json
import datetime

# Load violations JSON file
def load_violations():
    try:
        with open('violations.json', 'r') as f:
            data = json.load(f)
            results = data.get("result", [])
            # Create dataframe from violations
            df = pd.DataFrame([{
                "message": r.get("msg", ""),
                "policy": r.get("policy", "Unknown"),
                "resource": r.get("resource", "Unknown"),
                "severity": r.get("severity", "Medium"),
                "timestamp": datetime.datetime.now()  # In real app, parse actual timestamp
            } for r in results])
            return df
    except Exception as e:
        return pd.DataFrame()

# Main dashboard
st.title("PolicyGuard Compliance Dashboard")

df = load_violations()

if df.empty:
    st.info("No active violations found.")
else:
    st.metric("Active Violations", len(df))

    # Filter by policy type dropdown
    policy_filter = st.selectbox("Filter by Policy", ["All", "SOC2", "PCI", "HIPAA"])
    if policy_filter != "All":
        df_filtered = df[df['policy'].str.contains(policy_filter, case=False, na=False)]
    else:
        df_filtered = df

    st.dataframe(df_filtered)

    # Historical trends (fake example using counts by day)
    st.subheader("Violation Trends (Last 7 Days)")
    # Create fake data for demo - replace with actual historical data in real app
    today = datetime.datetime.now()
    trend_data = {
        "date": [today - datetime.timedelta(days=i) for i in range(6, -1, -1)],
        "violations": [5, 3, 4, 6, 2, 1, len(df_filtered)]
    }
    trend_df = pd.DataFrame(trend_data)
    trend_df['date'] = trend_df['date'].dt.date

    st.line_chart(trend_df.set_index('date')['violations'])

    # Export report
    if st.button("Export Report as CSV"):
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "compliance_report.csv", "text/csv")


