import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Bullet Enhancer", layout="centered")
st.title("🧠 AI Resume Bullet Enhancer")

st.markdown("""
Type a rough resume bullet point below and let AI suggest a polished, professional version tailored to your desired role.
""")

input_text = st.text_area("Your draft bullet point:", height=120)
role = st.text_input("Optional: Target job role (e.g., Software Engineer, Data Analyst):")

BACKEND_URL ="https://resume-4-on1x.onrender.com/suggest-bullets"   # Replace with your backend URL

if st.button("Enhance Bullet Point"):
    if not input_text.strip():
        st.warning("Please enter a bullet point to enhance.")
    else:
        with st.spinner("Enhancing with AI..."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    headers={"Content-Type": "application/json"},
                    json={"text": input_text, "role": role}
                )
                if response.status_code == 200:
                    suggestion = response.json().get("suggested_bullet", "No suggestion returned.")
                    st.success("✅ Suggested Bullet Point:")
                    st.markdown(f"> {suggestion}")
                else:
                    st.error("❌ Failed to get a suggestion. Try again later.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
