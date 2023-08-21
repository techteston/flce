import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Centrality Analysis",
    page_icon="",
)


hide_st_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)

st.title("The :red[Airport Centrality]")
st.subheader('Understanding the Most Import Airport in the US ')

df = pd.DataFrame()
uploaded_file = st.file_uploader("Upload an csv Flights File",type=['csv'])
if uploaded_file is not None:
    st.success('File Uploaded Successfully!', icon="✅")
#    st.balloons()
    try:
        df=pd.read_csv(uploaded_file)
    except:
        df=pd.read_csv(uploaded_file)

if len(df) > 0:
    with st.expander('Sample Records', expanded=False):
        df2 = df[0:9]
        st.dataframe(data=df2, width=None, height=None,hide_index=1)
  

