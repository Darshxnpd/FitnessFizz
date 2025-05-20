import google.generativeai as genai

genai.configure(api_key="AIzaSyBbln0QkNVkz5_rlc6lf4LHXYNbyxIIDaw")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Ask your Question: ",input())
print(response.text)