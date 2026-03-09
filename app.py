import streamlit as st
from datetime import datetime, timedelta

st.title("⏱️ Work Time + Leave Time Calculator")

# Required work time
required_hours = 8
required_minutes = 30
required_total_minutes = required_hours * 60 + required_minutes

# Initialize session state
if "num_inputs" not in st.session_state:
    st.session_state.num_inputs = 2


# Convert HH:MM → minutes
def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


# Convert minutes → HH:MM
def minutes_to_time(total_minutes):
    h = total_minutes // 60
    m = total_minutes % 60
    return f"{h:02d}:{m:02d}"


st.write("Enter completed work times in **HH:MM format** (Example: 02:15)")

times = []

# Dynamic inputs
for i in range(st.session_state.num_inputs):
    t = st.text_input(f"Enter Time {i+1} (HH:MM)", key=f"time_{i}")
    times.append(t)

# Add more time inputs
if st.button("➕ Add Another Time"):
    st.session_state.num_inputs += 1
    st.rerun()

# Current time input
current_time = st.time_input("Current Time")

# Calculate
if st.button("🧮 Calculate Work & Leave Time"):

    try:
        total_minutes = 0

        for t in times:
            total_minutes += time_to_minutes(t)

        # Total worked time
        worked_time = minutes_to_time(total_minutes)

        st.success(f"✅ Total Worked Time = {worked_time}")

        # Remaining work
        remaining_minutes = required_total_minutes - total_minutes

        if remaining_minutes <= 0:
            st.success("🎉 You have already completed your work hours!")
        else:
            st.write(
                f"Remaining Time: **{remaining_minutes//60}h {remaining_minutes%60}m**"
            )

            # Calculate leave time
            remaining_time = timedelta(minutes=remaining_minutes)
            current_datetime = datetime.combine(datetime.today(), current_time)

            leave_time = current_datetime + remaining_time

            st.success(
                f"🟢 You can leave at: **{leave_time.strftime('%I:%M %p')}**"
            )

    except:
        st.error("❌ Invalid input! Please use HH:MM format (Example: 02:30)")