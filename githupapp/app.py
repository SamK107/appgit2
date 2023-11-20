import streamlit as st 
import pandas as pd 
# import plotly.graph_objects as go

import content
def app():
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Initialize data to Dicts of series. 
        d = {'one': pd.Series([10, 20, 30, 40], 
                            index=['a', 'b', 'c', 'd']), 
            'two': pd.Series([10, 20, 30, 40], 
                            index=['a', 'b', 'c', 'd'])} 
        
        # creates Dataframe. 
        df = pd.DataFrame(d) 
        
        st.dataframe(df, use_container_width=True)
    with col2:
        
        content.app()
        
    # with col3:
    #     fig = px.bar(df, x='one', y='two')
        
    #     st.plotly_chart(fig, use_container_width=True)
    
app()