import streamlit as st
import pandas as pd
import pickle
import os
from PIL import Image
from matplotlib import image
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

#Page Heading
st.header(":black[Laptop Price Prediction]")


#absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
#absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
#absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH =os.path.join(dir_of_interest, "images", "laptop11.jpg")
imge= image.imread(IMAGE_PATH)
st.image(imge)


DATA_PATH = os.path.join(dir_of_interest, "data")

#Load data
DATA_PATH1=os.path.join(DATA_PATH, "laptop_price.csv")
df=pd.read_csv(DATA_PATH1)

data=df.copy()


#Accepting the required features from user

brand = st.selectbox(':green[ Laptop Brand]',(df['Company'].unique()))
    

operating_system=st.selectbox(':green[ Operating System]',(df['Operating System'].unique()))


processor=st.selectbox(':green[ Processor Type]',(df['Processor Type'].unique()))
    

ram_type=st.selectbox(':green[ RAM Type]',(df['RAM Type'].unique()))
    


ram_size=st.selectbox( ':green[ RAM Size]',(df['RAM size'].unique()))
    

disc_type=st.selectbox(':green[ DISC Type]',(df['Disc Type'].unique()))
    


disc_size=st.selectbox(':green[ DISC Size]',(df['Disc Size'].unique()))
    


#Create dataframe 
s=pd.DataFrame({"Company":[brand],"Operating System":[operating_system], "Processor Type":[processor], "RAM Type":[ram_type], "RAM size":[ram_size],"Disc Type":[disc_type], "Disc Size":[disc_size]})

#Convert these values to suitable integer form
#Function to change brand to number
def replace_brand(brand):
    if brand=='Lenovo':
        return 1
    elif brand=='ASUS':
        return 2
    elif brand=='HP':
        return 3
    elif brand=='DELL':
        return 4
    elif brand=='RedmiBook':
        return 5
    elif brand=='realme':
        return 6
    elif brand=='acer':
        return 7
    elif brand=='MSI':
        return 8
    elif brand=='APPLE':
        return 9
    elif brand=='Infinix':
        return 10
    elif brand=='SAMSUNG':
        return 11
    elif brand=='Ultimus':
        return 12
    elif brand=='Vaio':
        return 13
    elif brand=='GIGABYTE':
        return 14
    elif brand=='Nokia':
        return 15
    elif brand=='ALIENWARE':
        return 16  
data['Company']=data['Company'].apply(replace_brand)

#Function to change processor to number
def replace_processor(Processor):
    if Processor=='Intel':
        return 1
    elif Processor=='AMD':
        return 2
    elif Processor=='Apple':
        return 3
    elif Processor=='Qualcomm':
        return 4
data['Processor Type']=data['Processor Type'].apply(replace_processor)

#Function to change os to number
def replace_os(os):
    if os=='Windows 11':
        return 1
    elif os=='Windows 10':
        return 2
    elif os=='Mac':
        return 3
    elif os=='Chrome':
        return 4
    elif os=='DOS':
        return 5
data['Operating System']=data['Operating System'].apply(replace_os)

#Function to change ram type to number
def replace_ram_type(ram_type):
    if ram_type=='DDR4':
        return 1
    elif ram_type=='DDR5':
        return 2
    elif ram_type=='LPDDR4':
        return 3
    elif ram_type=='Unified':
        return 4
    elif ram_type=='LPDDR4X':
        return 5
    elif ram_type=='LPDDR5':
        return 6
    elif ram_type=='LPDDR3':
        return 7   
data['RAM Type']=data['RAM Type'].apply(replace_ram_type)

#Function to change ram size to number
def replace_ram_size(ram_size):
    if ram_size=='8 GB':
        return 1
    elif ram_size=='16 GB':
        return 2
    elif ram_size=='4 GB':
        return 3
    elif ram_size=='32 GB':
        return 4
    elif ram_size=='64 GB':
        return 5
data['RAM size']=data['RAM size'].apply(replace_ram_size)

#Function to disc type to number
def replace_disc_type(disc_type):
    if disc_type=='SSD':
        return 1
    elif disc_type=='HDD':
        return 2
    elif disc_type=='EMMC':
        return 3
data['Disc Type']=data['Disc Type'].apply(replace_disc_type)

#Function to change disc size to number
def replace_disc_size(disc_size):
    if disc_size=='256GB':
        return 1
    elif disc_size=='512GB':
        return 2
    elif disc_size=='1TB':
        return 3
    elif disc_size=='128GB':
        return 4
    elif disc_size=='64GB':
        return 5
    elif disc_size=='32GB':
        return 6
    elif disc_size=='2TB':
        return 7
data['Disc Size']=data['Disc Size'].apply(replace_disc_size)

#Split data into X and y
X=data.drop('MRP', axis=1).values
y=data['MRP'].values


#Train the model
XGB=XGBRegressor(learning_rate=0.15, n_estimators=50, max_leaves=0, random_state=42)
XGB.fit(X,y)

#Convert User input to suitable integer form
s['Company']=s['Company'].apply(replace_brand)
s['Operating System']=s['Operating System'].apply(replace_os)
s['Processor Type']=s['Processor Type'].apply(replace_processor)
s['RAM Type']=s['RAM Type'].apply(replace_ram_type)
s['RAM size']=s['RAM size'].apply(replace_ram_size)
s['Disc Type']=s['Disc Type'].apply(replace_disc_type)
s['Disc Size']=s['Disc Size'].apply(replace_disc_size)




#Prediction
if st.button('Predict'):
    price=XGB.predict(s)
    price=price[0].round(3)    
    st.subheader(":blue[Price of your laptop is :] :darkgreen[{}]".format("₹"+str(price)))
else:
    pass
