%%writefile app.py
import streamlit as st 
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit, 1)

# Create a random array of data that we will use for our y values
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter=alt.Chart(df).mark_point().encode(
    x='x',
    y='y'
)
st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)


st.markdown("""
The 5 changes I made were:
- I changed the shape of the data points to a diamond shape.
- I changed the color of the datapoints to blue. 
- I changed the title of the x axis and y axis to X Axis and Y axis.
- I made the scatterplot interactive.
- I changed the scatterplot to a binned scatterplot so you can see the density of the datapoints.
""")

scatter=alt.Chart(df).mark_point(color='blue',shape='diamond').encode( 
    alt.X('x', title= 'X Axis',bin=True),
    alt.Y('y', title= 'Y Axis', bin=True),
    size='count()',
).interactive()

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- I added a tooltip to the chart
- I just changed the axis titles from net_generation to Net Generation and year to Year.
"""
)



source = data.iowa_electricity()
st.write(source)
area = alt.Chart(source).mark_area().encode(
    x=alt.X("year:T", title='Year'),
    y=alt.Y("net_generation:Q", title='Net Generation'),
    color="source:N",
    tooltip=['source','year', 'net_generation']
)
st.altair_chart(area, use_container_width=True)
