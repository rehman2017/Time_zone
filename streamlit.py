# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
# Page Title and Fav icon
st.set_page_config(
    page_title="TIME ZONE APP",
    page_icon="🕒",
)
# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Africa/Cairo",
    "Africa/Johannesburg",
    "America/Chicago",
    "America/Toronto",
    "America/Mexico_City",
    "America/Sao_Paulo",
    "Asia/Hong_Kong",
    "Asia/Shanghai",
    "Asia/Singapore",
    "Asia/Seoul",
    "Asia/Bangkok",
    "Asia/Manila",
    "Pacific/Auckland",
    "Europe/Madrid",
    "Europe/Paris",
    "Europe/Moscow",
    "Europe/Rome",
    "Europe/Istanbul",
    "Europe/Athens",
    "America/Denver",
    "America/Phoenix",
    "America/Miami",
    "America/Bogota",
    "America/Lima",
    "America/Anchorage",
    "America/Honolulu",
    "Atlantic/Reykjavik",
    "Asia/Kuala_Lumpur",
    "Asia/Tehran",
    "Asia/Riyadh",
    "Asia/Jakarta",
    "Asia/Yangon",
    "Asia/Baghdad",
    "Asia/Beirut",
    "Asia/Taipei",
    "Asia/Ulaanbaatar",
    "Australia/Perth",
    "Australia/Adelaide",
    "Australia/Brisbane",
    "Australia/Darwin",
    "Pacific/Fiji",
    "Pacific/Honolulu",
    "Pacific/Tahiti",
    "Europe/Amsterdam",
    "Europe/Brussels",
    "Europe/Stockholm",
    "Europe/Warsaw",
    "Europe/Vienna",
    "Europe/Lisbon",
    "Europe/Zurich",
    "Europe/Copenhagen",
    "Europe/Dublin"
]
# Gradients for Selected Timezones
gradient_combos = [
    "#00ff87, #07f49e",
    "#f1515e, #fa9372",
    "#f1515e, #fa9372",
    "#00ff87, #07f49e",
] * len(TIME_ZONES)
# Main Heading
st.write("<h1 style='text-align: center;' >TIME ZONE APP 🕒</h1>",
         unsafe_allow_html=True)
# Create a multi-select dropdown for choosing time zones
selected_timezone = st.sidebar.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi", "Asia/Dubai",
                                             "Asia/Kolkata",])
st.write(":gray[Selected Timezones:]")
# Adjust in the Two Column
colA, colB = st.columns([1, 1])
# Display current time for selected time zones
for i, tz in enumerate(selected_timezone):
    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime(
        "📅%d-%b-%y🕒%H:%M %p")
    # Display only City Name remove After "/"
    index = tz.find("/")
    index = index + 1 if index > 0 else 0
    # Divide Column as per Reminder Even or Add
    if i % 2 == 0:
        with colA:
            st.markdown(
                f"<div style='display: flex;justify-content: center;align-items: center;background: linear-gradient(135deg, {gradient_combos[i]});padding: 8px 10px; margin: 2px 0px; border-radius: 5px;color: #0e1117;font-weight: 600;'>{tz[index:].replace("_", " ")}, {current_time}</div>", unsafe_allow_html=True)
    else:
        with colB:
            st.markdown(
                f"<div style='display: flex;justify-content: center;align-items: center;background: linear-gradient(135deg, {gradient_combos[i]});padding: 8px 10px; margin: 2px 0px; border-radius: 5px;color: #0e1117;font-weight: 600;'>{tz[index:].replace("_", " ")}, {current_time}</div>", unsafe_allow_html=True)

# Display Current Time
st.markdown(
    f"<p style='display: flex;justify-content: center;align-items: center;margin-top:15px;color:gray;'>Current Time:</p>", unsafe_allow_html=True)
current_time = datetime.now().time()
st.markdown(
    f"<div style='display: flex;justify-content: center;align-items: center;gap:10px;font-size: 85px;font-weight: 800;line-height: 35px;margin-bottom:20px;'>{current_time.strftime("%I<p>𓃊</p> %M<p>𓃊</p>%S")}</div>", unsafe_allow_html=True)

# Adjust in the Three Column
col1, col2, col3 = st.columns([3, 1, 3])
with col1:
    # Dropdown to select source timezone
    from_tz = st.selectbox(":gray[From Timezone]", TIME_ZONES, index=0)
with col2:
    # = Sign
    st.write("<h1 style='text-align: center;' >=</h1>",
             unsafe_allow_html=True)
with col3:
    # Dropdown to select target timezone
    to_tz = st.selectbox(":gray[To Timezone]", TIME_ZONES, index=1)

# Create convert button and handle conversion
if st.button("Convert Time"):
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time,
                          tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone and format it with AM/PM
    convert_time = dt.astimezone(
        ZoneInfo(to_tz)).strftime("📅%d-%b-%y🕒%H:%M %p")
    # Display the converted time with success message
    st.markdown(
        f"<div style='display: flex;justify-content: center;align-items: center;background: linear-gradient(135deg, #6710c2, #5460f9);padding: 8px 10px; margin: 2px 0px; border-radius: 5px;color: white;font-weight: 600;'>Converted Time from {from_tz} to {to_tz}, {convert_time}</div>", unsafe_allow_html=True)