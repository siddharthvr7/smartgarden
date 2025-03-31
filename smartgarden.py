import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyBJ5Fn-Bo-IEDTmubX-pRzz2HdOKEz6F_w")
model = genai.GenerativeModel('gemini-1.5-flash')


# Function to get response
def get_gemini_response(input_text):
    try:
        response = model.generate_content(input_text)
        return response.text if response and hasattr(response, 'text') else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title='Garden Lover❤')
st.sidebar.header("How far will you go for your plants?")
st.sidebar.write("Made with ❤")

st.header("🌿 I will predict the weather for you!")
st.subheader("Plants are our soul, and we know they are yours too!")
st.subheader("Enter temperature and humidity info:")

# Input Fields
temperature = st.number_input("Enter the temperature that's displayed the longest (°C):", value=25.0)
humidity = st.number_input("Enter the humidity (%) :", value=50.0)
region = st.text_input("Enter your region", placeholder="E.g., California, India, London")

# Generate Prompt
input_prompt = f"""
You are an expert weather predictor. The user has entered:
- Temperature: {temperature}°C
- Humidity: {humidity}%
- Region: {region}

Predict the *Temperature and Humidity for the next week* based on the region.
- Display the results in a *structured format* (day-wise forecast).
- *Give gardening instructions* based on the predicted weather.
- *Provide safety instructions* if necessary.
- Format numbers to *two decimal places*.
"""

# Prediction Button
submit = st.button("🌤 Predict")

if submit:
    st.subheader("📌 Here are the results:")
    response = get_gemini_response(input_prompt)
    st.write(response)