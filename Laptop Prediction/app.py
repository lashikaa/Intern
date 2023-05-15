import streamlit as st
from PIL import Image
from matplotlib import image
import os
import pickle

#Title of the home page
st.header(":black[Laptop Price Prediction]")



#Adding image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "laptop head.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)


st.markdown(":lightblue[Lets Buy a new laptop for Data Science..!]")




    



