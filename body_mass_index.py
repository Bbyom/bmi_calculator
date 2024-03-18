import streamlit as st
st.title(':red[Abayomi\'s BMI calculator]')
from PIL import Image
img = st.image("C:\\Users\VP\Pictures\\baboon-yankari-2-042512_thumb.jpg")

st.text('BMI is a measurement of a person\'s leanness or corpulence based on their height and weight, and is intended to quantify tissue mass.\nIt is widely used as a general indicator of whether a person has a healthy body weight for their height.'
        '\nSpecifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between.\nThese ranges of BMI vary based on factors.')

weight = st.number_input("Enter your weight(in kgs)")
status = st.radio('select your height format:',('cms','meters', 'feet'))

if (status == 'cms'):
        height = st.number_input('centimetres')

        try:
            bmi = weight /((height/100)**2)
        except:
             st.text("enter some value of height")
elif (status == 'feet'):
        height = st.number_input('feet')

        try:
            bmi = weight /((height/3.28)**2)
        except:
             st.text("enter some value of height")

else:
    height = st.number_input('meters')

    try:
        bmi = weight / ((height ** 2))
    except:
        st.text("enter some value of height")

if (st.button('Calculate BMI')):
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))

    # give the interpretation of the BMI index
    if (bmi < 16):
        st.error("You are extremely underwight")
    elif( bmi >= 16 and bmi < 18.5):
        st.warning("You are underweight")

    elif( bmi  >= 18.5 and bmi  < 25):
        st.success("healthy")

    elif( bmi >= 25 and bmi < 30):

        st.warning("Overweight")

    elif( bmi >= 30):
        st.error("extremely overweight")

