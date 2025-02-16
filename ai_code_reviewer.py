import streamlit as st
import google.generativeai as ai

f = open('/content/key.txt')
key = f.read()
print(key)
ai.configure(api_key="key")

sys_prompt = """You are an advanced AI Code Reviewer.
You will receive code snippets in various programming languages.
Your task is to analyze the code, find improvements, find bugs, suggest optimizations, 
and highlight potential issues with explanations.
Provide detailed and professional feedback.
"""

# Load Gemini model
model = ai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=sys_prompt)

st.set_page_config(page_title="AI Code Reviewer", page_icon="💻", layout="wide")

st.title("👨‍💻 AI-Powered Code Reviewer")
st.markdown("### Upload your code, and get instant feedback with AI!")

# Sidebar for Navigation
with st.sidebar:
    st.header("📝 Choose Your Preferred Programming Language")  
    code_language = st.selectbox("Programming Language Selection:", ["Python", "JavaScript", "Java", "C++", "Other"])  
    st.markdown("---")
    st.info("This AI will analyze your code and provide correct code and feedback on your code.")

user_program = st.text_area("Paste your code below:", height=300, placeholder="Enter your code here...")

btn_click = st.button("🚀 Review Code")

if btn_click and user_program.strip():
    with st.spinner("Analyzing your code... ⏳"):
        user_prompt = f"Language: {code_language}\nCode:\n{user_program}\n\nReview this code with improvements, suggestions, and issues."
        response = model.generate_content(user_prompt)
        
        st.subheader("📝 Code Review & Feedback")
        st.write(response.text)

st.markdown("---")
st.caption("🤖 Built with Streamlit & Gemini Api - 👨‍💻 AI-Powered Code Reviewer")
