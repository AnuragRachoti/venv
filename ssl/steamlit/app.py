import streamlit as st

import pandas as pd
import numpy as np

##Title  of the application

st.title('Hello streamlit')

##displaying the simple text

st.write('this is the introduction to machine learning')

# dataframe printing.

df = pd.DataFrame({
    'first_column' : [1,2,3,4,5],
    'second_column': [2,3,4,5,6]
})


#displaying the dataframe.

st.write('displaying the dataframe')
st.write(df)

#creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)

st.line_chart(chart_data)