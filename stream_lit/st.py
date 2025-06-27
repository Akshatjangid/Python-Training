## Streamlit 
## pyhon lib
## webpagaes for ml and data science project
## html and css no requirnment
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns
import altair as alt
import time

# st.title("hello world")
# st.header("1. Text elements")
# st.subheader("markdown,code,latex")
# st.markdown("**bold text**,*italic text*,`code`")
# st.code("print('hello everyone ')", language="python")
# st.latex(r"a^2 + b^2 = c^2 ")


st.divider()

# # metrices and message
# st.header("2. metrices and message")
# st.metric(label="Revenue",value=1234,delta="+10%",delta_color="inverse")
# st.error("this is an error message")
# st.warning("this is an warning message")
# st.info("this is an info message")
# st.success("this is an success message")
# st.exception(ValueError("this is an exception message"))

# st.divider()
# st.header("3. data display")
# df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
# st.dataframe(df)
# st.table(df)

# if we have to use in json format
# st.json(df.to_dict())

# #chart
# st.header("4. chart")
# st.line_chart(df)
# st.bar_chart(df)
# st.area_chart(df)

# chart=alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
# st.altair_chart(chart,use_container_width=True)
# fig , ax=plt.subplots()
# ax.plot(df.index,df.a)
# st.pyplot(fig)

st.divider()
st.header("5. widget")
with st.form("input form"):
    name=st.text_input("enter your name")
    age=st.number_input(" enter your age")
    mood=st.radio("select your mood",("happy","sad","neutral"))
    language=st.multiselect("select your language",("english","french","german"))
    submit=st.form_submit_button("submit")
    if submit :
        st.success(f"Name:{name},Age:{int(age)},Mood : {mood},:Language:{language},Submiteed:{submit}")


col1,col2,col3=st.columns(3)
with col1:
    st.text_input("enter your name")
    st.number_input(" enter your age")
with col2:
        st.radio("select your mode",("happy","sad","neutral"))
        st.multiselect("select your language",("english","french","german"))
with col3:
            st.title("output")

col1,col2=st.columns(2)
with col1:
    number=st.slider("select a number",0,100)
with col2:
      colour=st.color_picker ("select a colour","#FAF9F6")

st.text_area("Enter your message")
st.date_input("Enter  Date")
st.time_input("Enter Time")
st.file_uploader("Enter your File")

st.divider()
#media
st.header("6, Media")
st.image(r"C:\Users\Akshat\OneDrive\Pictures\zebra.jpeg", caption="random image")

st.video("https://www.w3school.com/html/mov_bbb.mp4")
# st.audio("")
option = st.sidebar.select_slider("Select an option", options=["option 1", "option 2"])

with st.container():
      st.write("this is a container")
with st.expander("expander header"):
      st.write("expander hader")
with st.spinner("Loading Data"):
      time.sleep(10)

#st.sucess("data loaded")
st.toast("toast message",icon="👍")
st.page_link("https://streamlit.io",label="streamlit website",icon="📃")