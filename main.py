import streamlit as st

# Unit conversion factors
conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462,
        "Ounce": 35.274,
    },
    "Temperature": {},  # Special case, handled separately
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    factor_from = conversion_factors[category][from_unit]
    factor_to = conversion_factors[category][to_unit]
    return value * (factor_to / factor_from)

# Streamlit UI
st.title("Unit Converter")

category = st.selectbox("Select Conversion Category", list(conversion_factors.keys()))

units = list(conversion_factors[category].keys())
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
value = st.number_input("Enter value", min_value=0.0, format="%.2f")
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
