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