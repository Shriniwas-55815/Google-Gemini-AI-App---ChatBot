## - Function to load gemini model and get respones

def get_gemini_response(question):

model = genai.GenerativeModel('gemini-2.0-flash-exp')

response = model.generate_content(question)

return response.text

##initialize our streamlit app

st.set_page_config(page_title="GEMINI LLM APP")

st.header("Gemini AI BOT Application")

input=st.text_input("Input: ",key="input")

submit=st.button("click me to generate response")

##If ask button is clicked

if submit:

response=get_gemini_response(input)

st.subheader("The Response is")

st.write(response)