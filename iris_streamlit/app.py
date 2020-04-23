# importing key modules
import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance

# Title and Subheader for start of app

st.title("A Simple App using Iris Dataset")
st.text("using Streamlit")
st.header("Exploratory Data Analysis")

# Loading data

my_dataset = "iris.csv"

# To Improve speed and cache data

@st.cache(persist=True)

# define function for reading data

def load_data(dataset):
	df = pd.read_csv(os.path.join(dataset))
	return df

# Show Dataset top values and last values

if st.checkbox("Preview DataFrame"):
	data = load_data(my_dataset)
	if st.button("First 5 rows"):
		st.write(data.head())
	if st.button("Last 5 rows"):
		st.write(data.tail())
	else:
		st.write(data.head(2))

# Show No. of features in Data

if st.checkbox("Show All Features' Name"):
	data = load_data(my_dataset)
	st.text("Features in Data")
	st.write(data.columns)


# Dimensions

if st.checkbox("Show me Dimensions of my Data"):
    data_dim = st.radio('What Dimension Do You Want to Show', ('Rows', 'Columns'))
    if data_dim == 'Rows':
        data = load_data(my_dataset)
        st.text("Showing Length of Rows")
        st.write(len(data))
    if data_dim == 'Columns':
        data = load_data(my_dataset)
        st.text("Showing Length of Columns")
        st.write(data.shape[1])

# Summary

if st.checkbox("Show Summary of Dataset"):
	data = load_data(my_dataset)
	st.write(data.describe())

# Selection
if st.checkbox("Show each feature"):
    species_option = st.selectbox('Select Columns',('sepal_length','sepal_width','petal_length','petal_width','species'))
    data = load_data(my_dataset)
    if species_option == 'sepal_length':
	    st.write(data['sepal_length'])
    elif species_option == 'sepal_width':
	    st.write(data['sepal_width'])
    elif species_option == 'petal_length':
	    st.write(data['petal_length'])
    elif species_option == 'petal_width':
	    st.write(data['petal_width'])
    elif species_option == 'species':
	    st.write(data['species'])
    else:
	    st.write("Select A Column")

# Show Plots

if st.checkbox("Simple  Plot with Matplotlib "):
	data = load_data(my_dataset)
	data.plot()
	st.pyplot()

# Show Correlation Plots

if st.checkbox("Simple Correlation Plot with Seaborn "):
	data = load_data(my_dataset)
	st.write(sns.heatmap(data.corr(),annot=True))
	# Use Matplotlib to render seaborn
	st.pyplot()

# Show Plots

if st.checkbox("Bar Plot of Groups/Counts"):
	data = load_data(my_dataset)
	v_counts = data.groupby('species')
	st.bar_chart(v_counts)

# Iris Image Manipulation
@st.cache
def load_image(img):
	im =Image.open(os.path.join(img))
	return im

# Image Type
species_type = st.radio('What is the Iris Species do you want to see?',('Setosa','Versicolor','Virginica'))

if species_type == 'Setosa':
	st.text("Showing Setosa Species")
	st.image(load_image('iris-setosa.jpg'))
elif species_type == 'Versicolor':
	st.text("Showing Versicolor Species")
	st.image(load_image('iris_versicolor.jpg'))
elif species_type == 'Virginica':
	st.text("Showing Virginica Species")
	st.image(load_image('iris_virginica.jpg'))

# Show Image
if st.checkbox("Show Image/Hide Image"):
	my_image = load_image('iris-setosa.jpg')
	enh = ImageEnhance.Contrast(my_image)
	num = st.slider("Set Your Contrast Number",1.0,3.0)
	img_width = st.slider("Set Image Width",300,500)
	st.image(enh.enhance(num),width=img_width)
