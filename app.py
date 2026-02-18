import streamlit as st

st.title("⏱️ Time Addition Calculator")

# Initialize session state for number of inputs
if "num_inputs" not in st.session_state:
    st.session_state.num_inputs = 2

# Function to convert HH:MM into minutes
def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

# Function to convert minutes back to HH:MM
def minutes_to_time(total_minutes):
    h = total_minutes // 60
    m = total_minutes % 60
    return f"{h:02d}:{m:02d}"

st.write("Enter times in **HH:MM** format (Example: 02:15)")

times = []

# Dynamic time input fields
for i in range(st.session_state.num_inputs):
    t = st.text_input(f"Enter Time {i+1} (HH:MM)", key=f"time_{i}")
    times.append(t)

# Button to add another time input
if st.button("➕ Add Another Time"):
    st.session_state.num_inputs += 1
    st.rerun()

# Button to calculate total time
if st.button("🧮 Calculate Total Time"):
    try:
        total = 0
        for t in times:
            total += time_to_minutes(t)

        result = minutes_to_time(total)
        st.success(f"✅ Total Time = {result}")

    except:
        st.error("❌ Invalid input! Please enter all times in HH:MM format (Example: 04:30)")
