import streamlit as st
import pandas as pd
import networkx as nx

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

st.title(":red[Airport Centrality]")
st.subheader('Understanding the Most Import Airport by flights')

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
        # Create a directed graph from the flight data
        G = nx.DiGraph()
        # Add nodes (airports)
        li_airports = pd.unique(df["DESTINATION_AIRPORT_NAME"])
        df_airports = pd.DataFrame(li_airports)
        li_airports = pd.unique(df["ORIGIN_AIRPORT_NAME"])
        df_airports2 = pd.DataFrame(li_airports)
        df_airports = pd.concat([df_airports, df_airports2], ignore_index=True)
        df_airports.drop_duplicates(subset=0,inplace=True)
        airports = df_airports[0].unique()
        G.add_nodes_from(airports)
        for _, row in df.iterrows():
            G.add_edge(row['ORIGIN_AIRPORT_NAME'], row['DESTINATION_AIRPORT_NAME'])
        st.dataframe(data=df2, width=None, height=None,hide_index=1)

if st.button('Airport Centrality'):
    degree_centrality = nx.degree_centrality(G)
    degree_centrality_df = pd.DataFrame.from_dict(degree_centrality, orient='index', columns=['Degree Centrality'])
    degree_centrality_df.sort_values(by=["Degree Centrality"],ascending=False,inplace=True)
    degree_centrality_df_top = degree_centrality_df[0:9]
    st.caption("The Airports with the Most Connections 	:small_airplane:")
    st.dataframe(data=degree_centrality_df_top, width=None, height=None,hide_index=1)

    betweenness_centrality = nx.betweenness_centrality(G)
    betweenness_centrality_df = pd.DataFrame.from_dict(betweenness_centrality, orient='index', columns=['Degree Centrality'])
    betweenness_centrality_df.sort_values(by=["Degree Centrality"],ascending=False,inplace=True)
    betweenness_centrality_df_top = betweenness_centrality_df[0:9]
    st.caption("The Airports with the Most Transits :airplane_departure:")
    st.dataframe(data=betweenness_centrality_df_top, width=None, height=None,hide_index=1)

    closeness_centrality = nx.closeness_centrality(G)
    closeness_centrality_df = pd.DataFrame.from_dict(closeness_centrality, orient='index', columns=['Degree Centrality'])
    closeness_centrality_df.sort_values(by=["Degree Centrality"],ascending=False,inplace=True)
    closeness_centrality_df_top = closeness_centrality_df[0:9]
    st.caption("The Airports with the Most Accessibility :airplane_arriving:")
    st.dataframe(data=closeness_centrality_df_top, width=None, height=None,hide_index=1)

    eigenvector_centrality = nx.eigenvector_centrality(G)
    pagerank = nx.pagerank(G)