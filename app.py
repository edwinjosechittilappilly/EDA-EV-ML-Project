import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("EV Data Analysis and Recommendation System ")
st.write("Mentor: Alvis Fong")

st.write("This is a project to analyze the data of Electric Vehicles and recommend the best EV for the user based on their requirements.")


st.sidebar.success("""
Collaborators:
 - [Surya Sudarshan Ryali](https://www.linkedin.com/in/surya-sudarshan-ryali-38454b161/)
 - [Prabhas Reddy](https://www.linkedin.com/in/kprabhasreddy/)
 - [Braden Draucek](https://www.linkedin.com/in/braden-draucek-746949196/)
 - [Edwin Jose](https://www.linkedin.com/in/edwinjosechittilappilly/)
""")

st.markdown("""
Collaborators:

 - [Surya Sudarshan Ryali](https://www.linkedin.com/in/surya-sudarshan-ryali-38454b161/)
 - [Prabhas Reddy](https://www.linkedin.com/in/kprabhasreddy/)
 - [Braden Draucek](https://www.linkedin.com/in/braden-draucek-746949196/)
 - [Edwin Jose](https://www.linkedin.com/in/edwinjosechittilappilly/)
""")
            
st.markdown('<a href="/carInsights" target="_self">Next page</a>', unsafe_allow_html=True)




footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/edwinjosechittilappilly/" target="_blank">EJ</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)