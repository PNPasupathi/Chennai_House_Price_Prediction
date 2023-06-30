import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )
add_bg_from_local('Images/bg2.jpg')

st.title('')
st.markdown("<h2 style= 'color: #FF0000;font-size: 46px;font-family:Arial ;font-weight: bold;'> <strong>Chennai House Price Prediction</strong></h2>", unsafe_allow_html=True)

st.markdown('#')

scaler=pickle.load(open('scaler.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))


st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Area</h2>", unsafe_allow_html=True)
area=st.selectbox('',['Karapakkam','Anna Nagar','Adyar','Velachery','Chrompet','KK Nagar','T Nagar'])
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Square Feet</h2>", unsafe_allow_html=True)
sqft=st.number_input('',min_value=100)
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Number of Bedroom</h2>", unsafe_allow_html=True)
nbedroom=st.number_input('',min_value=2)
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Number of BathRoom</h2>", unsafe_allow_html=True)
nroom=st.number_input('',min_value=0)
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Select the Sale Condition</h2>", unsafe_allow_html=True)
sale_cond=st.selectbox('',['AbNormal','Family','Partial','AdjLand','Normal Sale'])
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Is Parking Available or Not</h2>", unsafe_allow_html=True)
park_faci=st.selectbox('',['Yes','No'])
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Build Type</h2>", unsafe_allow_html=True)
build_type=st.selectbox('',['Commercial','Others','House'])
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Choose the Utility Option</h2>", unsafe_allow_html=True)
utility=st.selectbox('',['All Pub','ELO','NoSeWa'])
st.markdown("<h2 style= 'color: white;font-size: 22px;'>How is Street Outside that House</h2>", unsafe_allow_html=True)
street=st.selectbox('',['Paved','Gravel','No Access'])
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Select your Preferable Zone</h2>", unsafe_allow_html=True)
zone=st.selectbox('',['A','RH','RL','I','C','RM'])
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Registration Fees</h2>", unsafe_allow_html=True)
regfee=st.number_input(' ',min_value=0)
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Commision Fees</h2>", unsafe_allow_html=True)
commfee=st.number_input('',min_value=10000)
st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Year of Sale</h2>", unsafe_allow_html=True)
year=st.number_input('',min_value=2000)

btn1,btn2,btn3=st.columns([2,1,2])
with btn2:
    st.write('')
    predbtn=st.button('Predict')

def conarea(area):
    if area=='Karapakkam':
        return 0
    elif area=='Anna Nagar':
        return 1
    elif area=='Adyar':
        return 2
    elif area=='Velachery':
        return 3
    elif area=='Chrompet':
        return 4
    elif area=='KK Nagar':
        return 5
    elif area=='T Nagar':
        return 6

def consalecon(x):
    if x=='AbNormal':
        return 0
    elif x=='Family':
        return 1
    elif x=='Partial':
        return 2
    elif x=='AdjLand':
        return 3
    elif x=='Normal Sale':
        return 4

def conpark(park):
    if park=='Yes':
        return 1
    elif park=='No':
        return 0

def conbuild(type):
    if type=='Commercial':
        return 0
    elif type=='Others':
        return 1
    elif type=='House':
        return 2

def conutilavail(x):
    if x=='All Pub':
        return 0
    elif x=='ELO':
        return 1
    elif x=='NoSeWa':
        return 2

def constreet(street):
    if street=='Paved':
        return 0
    elif street=='Gravel':
        return 1
    elif street=='No Access':
        return 2

def conzone(zone):
    if zone=='A':
        return 0
    elif zone=='RH':
        return 1
    elif zone=='RL':
        return 2
    elif zone=='I':
        return 3
    elif zone=='C':
        return 4
    elif zone=='RM':
        return 5

newarea=conarea(area)
sale_cond=consalecon(sale_cond)
park_faci=conpark(park_faci)
build_type=conbuild(build_type)
utility=conutilavail(utility)
street=constreet(street)
zone=conzone(zone)
if predbtn==True:
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
            unsafe_allow_html=True
        )


    add_bg_from_local('Images/{}.jpg'.format(area))
    value=scaler.transform(np.array([newarea,sqft,nbedroom,nroom,sale_cond,park_faci,build_type,utility,street,zone,regfee,commfee,year]).reshape(1,-1))
    result=model.predict(value)
    res1,res2,res3=st.columns([0.5,2,0.3])
    with res2:
        st.markdown(
            "<h2 style= 'color: #FFE000;background-color:black;font-size: 46px;font-family:Arial ;font-weight: bold;'> <strong>Amount : Rs {} </strong></h2>".format(round(result[0])),
            unsafe_allow_html=True)
