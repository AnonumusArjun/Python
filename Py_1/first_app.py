import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time

st.write("---------------")
st.title('My first app')


st.write("---------------")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4, 5,6],
    'second column': [10, 20, 30, 40,50,60]
}))

st.write("---------------")
df = pd.DataFrame({
  '1st column': [1, 2, 3, 4],
  '2nd column': [10, 20, 30, 40]
})

df


st.write("---------------")
st.title("Draw Line chart...")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)




st.write("---------------")
st.title("Plot a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns= ['lat', 'lon'])
st.map(map_data)

st.write("---------------")
st.title("Put widgets in a sidebar")
option = st.selectbox(
    'Which number do you like best?',
     df['1st column'])


'You selected: ', option

st.write("---------------")
st.title("Show progress")
' Starting long computation'
#add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(.005)# 0.1

'....and now we \`re done !'



st.write("---------------")
st.title("Content")
import streamlit as st
x = 4
st.write(x, 'squared is', x * x)


st.write("---------------")
x = st.slider('x') # This is widget
st.write(x, 'squared is', x*x)


st.write("---------------")

# Add a selectbox to the sidebar:
st.title('Check box')
add_selectbox = st.write(st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home Phone', 'enrollment Num')
))

# Add a slider to the slider:
st.title('slider')
add_slider =  st.write(st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
))


st.write("---------------")
st.title('Caching')
@st.cache
def my_slow_function(argq,arg2):
    return the_output


st.write("---------------")
st.write("---------------")
st.write("---------------")
st.title('Fetch some data')
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')





