## Streamlit 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns
import altair as alt

st.title("hello world")
st.header("1. Text elements")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,`code`")
st.code("print('hello everyone ')", language="python")
st.latex(r"a^2 + b^2 = c^2 ")


st.divider()

# metrices and message
st.header("2. metrices and message")
st.metric(label="Revenue",value=1234,delta="+10%",delta_color="inverse")
st.error("this is an error message")
st.warning("this is an warning message")
st.info("this is an info message")
st.success("this is an sucess message")
st.exception(ValueError("this is an exception message"))

st.divider()
st.header("3. data display")
df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df)

# if we have to use in json format
st.json(df.to_dict())

#chart
st.header("4. chart")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

chart=alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax=plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)

st.divider()