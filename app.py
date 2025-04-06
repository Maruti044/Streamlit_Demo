import streamlit as st
import pandas as pd
import numpy as np
import time


st.title("Welcon to Nepal in 2025")
st.write("Nepal, nestled between China and India, spans a diverse landscape from the Himalayan mountains to fertile plains, covering an area slightly larger than Arkansas. Its population stands at 29.6 million, with a density of 206.61 per km², and a slight annual decline of 33,000, or 0.45%. The demographic breakdown shows a male-to-female ratio of 0.92 to 1, with median ages of 24.56 for males and 27.32 for females.")

# Input Widgets
# Button Implementation
button_clicked = st.button("Submit", type="primary")
if button_clicked:
    st.write("Button Clicked!")

button_clicked = st.button("Submit", type="secondary")
# checkbox Implementation
checkbox_selected = st.checkbox("Select this option")
if checkbox_selected:
    st.write("Checkbox selected")
# radio button Implementation
radio_option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selected option: {radio_option}")   
# selectbox Implementation
select_option = st.selectbox("Select a value:", ["A", "B", "C"])
st.write(f"Selected value: {select_option}")
# multiselect Implementation
multi_select_options = st.multiselect("Select multiple values:", ["Apple", "Banana", "Cherry", "Date"])
st.write(f"Selected values: {multi_select_options}")
# slider Implementation
slider_value = st.slider("Select a range:", 0, 100, (25, 75))
st.write(f"Selected range: {slider_value}")
# text_input Implementation
text_input_value = st.text_input("Enter some text:")
st.write(f"You entered: {text_input_value}")
# text_area Implementation
text_area_value = st.text_area("Enter a multi-line text:")
st.write(f"You entered: {text_area_value}")
# number_input Implementation
number_input_value = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
st.write(f"You entered: {number_input_value}")

# date and time  Implementation
date_input_value = st.date_input("Select a date:")
st.write(f"Selected date: {date_input_value}")

time_input_value = st.time_input("Select a time:")
st.write(f"Selected time: {time_input_value}")
# file_uploade  Implementation
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
# color_picker  Implementation
color_picked = st.color_picker("Pick a color")
st.write(f"Picked color: {color_picked}")


# Display Elements
st.header("Display Elements")

st.write("This is some text displayed using st.write.")
st.markdown("**This is bold text using Markdown.**")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.code("print('Hello, Streamlit!')", language="python")
st.json({"name": "John", "age": 30})


df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
st.dataframe(df)
st.table(df.head())


st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
st.audio("https://file-examples.com/storage/fe99232c7e6301519082f42/2017/11/file_example_MP3_700KB.mp3")
st.video("https://file-examples.com/storage/fe99232c7e6301519082f42/2017/04/file_example_MP4_480_1_5MG.mp4")



progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)
st.success('Done!')



with st.status('Downloading data...', expanded=True) as status:
    st.write("Finding data...")
    time.sleep(2)
    st.write("Loading data...")
    time.sleep(2)
    st.write("Saving data...")
    status.update(label="Download complete!", state="complete", expanded=False)





    # Layout Elements
st.header("Layout Elements")

col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
    st.slider("Slider in Column 1", 0, 10)
with col2:
    st.write("Column 2")
    st.selectbox("Select in Column 2", ["A", "B"])

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content in Tab 1")
with tab2:
    st.write("Content in Tab 2")

with st.expander("Expand this section"):
    st.write("This content is hidden until expanded.")

st.sidebar.header("Sidebar Controls")
sidebar_slider = st.sidebar.slider("Sidebar Slider", 0, 10)
st.sidebar.write(f"Sidebar slider value: {sidebar_slider}")

empty_space = st.empty()
empty_space.write("This will be replaced.")
time.sleep(2)
empty_space.write("Replaced!")