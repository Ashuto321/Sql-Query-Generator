from langchain_text_splitters import Language
import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyAF5OrzBLMMZP5o3gi66GxaPWRhLkSh1o4"

genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')


def main():
       
       st.set_page_config(page_title="Edureka SQL Query Generator 📝", page_icon=":robot:")

       col1, col2, col3 = st.columns([1, 2, 1])

       with col2:
    # Display both images with the same width
         st.image("edureka.png", width=200)
         st.image("sql_logo.jpg", width=200)
 
       st.markdown(
               """
              <div style ="text-align:center">
              <h1>SQL Query Generator 📚</h1>
              <h3> I can generate SQL queries for you!📝</h3>
              <h4> With Explanation as well!! </h4>
              <p> This tool is allows you to generate SQL queries based on your data. </p>

              </div>
              """,
              unsafe_allow_html=True,

)
       
       text_input=st.text_area("Enter your query here in plain English:  ")

     

       submit_button=st.button("Generate SQL Query")
       
       if submit_button:
              with st.spinner("Generating SQL Query...."):
                     template="""
                          Create a SQL query Snippet using the below text:

                          ....
                               {text_input}
                          ....
                           I just want a SQL Query .

                         """   
                     formatted_template=template.format(text_input=text_input)  
                     st.write(formatted_template)
                     response=model.generate_content(formatted_template)
                     sql_query=response.text
                     sql_query = sql_query.strip().lstrip("```sql").rstrip("```")

                     expected_output="""
                         What would be the expected response of this SQL query snippet:
                          ....
                               {sql_query}
                          ....
                           Provide sample tabular response with no explanation:

                         """         
                     expected_output_formatted=expected_output.format(sql_query=sql_query)
                     eoutput=model.generate_content(expected_output_formatted)
                     eoutput=eoutput.text
                     st.write(eoutput)
                     explanation="""
                        Explain this SQL Query:
                          ....
                               {sql_query}
                          ....
                           please Provide with simplest of explanation:


                         """  
                     explanation_formatted=explanation.format(sql_query=sql_query)
                     explanation=model.generate_content(explanation_formatted)
                     explanation=explanation.text
                     st.write(explanation)

                     with st.container():
                            st.success("SQL Query Generated successfully! Here is your query below")
                            st.code(sql_query, language="sql")

                            st.success("Expected Output of this SQL Query will be: ")
                            st.markdown(eoutput)

                            st.success("Explanation of this SQL Query:")
                            st.markdown(explanation)

main()         
