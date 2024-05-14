import streamlit as st
import pickle
import pandas as pd
import sklearn

# Load the trained machine learning model
model=pickle.load(open(r'C:\Users\samar\Downloads\diabetes.sav','rb'))

# Title and information about the app
st.title('Diabetes Prediction app')
st.info('Application for Diabetes Predection Disease')

# Sidebar for feature selection
st.sidebar.header('Feature Selection')

# Text inputs for user to input features
Pregnancies=st.text_input('Pregnancies')
Glucose=st.text_input('Glucose')
BloodPressure=st.text_input('BloodPressure')
SkinThickness=st.text_input('SkinThickness')
Insulin=st.text_input('Insulin')
BMI=st.text_input('BMI')
DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
Age=st.text_input('Age')
NewBMI_Obesity1=st.text_input('NewBMI_Obesity 1')
NewBMI_Obesity2=st.text_input('NewBMI_Obesity 2')
NewBMI_Obesity3=st.text_input('NewBMI_Obesity 3')
NewBMI_Overweight=st.text_input('NewBMI_Overweight')
NewBMI_Underweight=st.text_input('NewBMI_Underweight')
NewInsulinScore_Normal=st.text_input('NewInsulinScore_Normal')
NewGlucose_Low=st.text_input('NewGlucose_Low')
NewGlucose_Normal=st.text_input('NewGlucose_Normal')
NewGlucose_Overweight=st.text_input('NewGlucose_Overweight')
NewGlucose_Secret=st.text_input('NewGlucose_Secret')

# Create a dataframe with the user input
df=pd.DataFrame({'Pregnancies':[Pregnancies],'Glucose':[Glucose],
'BloodPressure':[BloodPressure], 'SkinThickness':[SkinThickness],
'Insulin':[Insulin],'BMI':[BMI],'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
'Age':[Age],'NewBMI_Obesity 1':[NewBMI_Obesity1],'NewBMI_Obesity 2':[NewBMI_Obesity2],'NewBMI_Obesity 3':[NewBMI_Obesity3],'NewBMI_Overweight':[NewBMI_Overweight],
'NewBMI_Underweight':[NewBMI_Underweight],'NewInsulinScore_Normal':[NewInsulinScore_Normal],'NewGlucose_Low':[NewGlucose_Low],'NewGlucose_Normal':[NewGlucose_Normal],
'NewGlucose_Overweight':[NewGlucose_Overweight],'NewGlucose_Secret':[NewGlucose_Secret]},index=[0])

# Button to confirm user input
Con=st.sidebar.button('confirm')

if Con:
# Predict using the trained model
    result=model.predict(df)
    if result == 0:
        st.sidebar.write('Non Diabetic')
# Show an image for non-diabetic prediction
        st.sidebar.image('https://www.shaalaa.com/images/_4:75baa69994114e7ca914cc0096fd8253.png',width=250)
    else:
        st.sidebar.write('Diabetic')
# Show an image for diabetic prediction
        st.sidebar.image('https://wallpaperaccess.com/full/3702009.jpg',width=250)









