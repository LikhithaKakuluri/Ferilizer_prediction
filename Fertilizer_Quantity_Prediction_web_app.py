import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model=pickle.load(open("C:/Users/kakul/streamlit/Fertilizer_prediction/Fertilizer_model.sav",'rb'))

img = '''
<style>
.stApp {
    background-image: url("https://bmkltsly13vb.compat.objectstorage.ap-mumbai-1.oraclecloud.com/cdn.dailymirror.lk/assets/uploads/image_d30a1b9be7.jpg");
    background-size: cover;
    background-position: top center;
    background-repeat: no-repeat;
    background-attachment: local;
}
</style>
'''
st.markdown(img, unsafe_allow_html=True)

#creating a function for prediction

def fertilizer_prediction(input_data):
    
    #changing the input data to numpy array
    input_data_as_numpy_array=np.array(input_data,dtype=float)
    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    predictions=loaded_model.predict(input_data_reshaped)
    for prediction in predictions:
        return f'N: {prediction[0]}\n P: {prediction[1]}\n K: {prediction[2]}'



def main():
    #page title
    st.title("Fertilizer Prediction Using ML")

    temperature=st.text_input("Enter the temperature in degree Celsius")

    humidity=st.text_input("Enter the  relative humidity in percentage")

    ph=st.text_input("Enter the ph value of the soil")

    rainfall=st.text_input("Enter the rainfall in mm")

    crop_labels = {
    0: 'Apple', 1: 'Banana', 2: 'Blackgram', 3: 'Chickpea', 4: 'Coffee',
    5: 'Coconut', 6: 'Cotton', 7: 'Grapes', 8: 'Jute', 9: 'Kidneybeans',
    10: 'Lentil', 11: 'Maize', 12: 'Mango', 13: 'Mothbeans', 14: 'Mungbean',
    15: 'Muskmelon', 16: 'Orange', 17: 'Papaya', 18: 'Pigeonpeas', 19: 'Pomegranate',
    20: 'Rice', 21: 'Watermelon'}
    # User input for the crop label
    label = st.text_input("Enter the label of the crop")
    # Display the corresponding crop name if a valid numeric label is entered
    try:
        label = int(label)
        if label in crop_labels:
            st.write(f"The corresponding crop for label {label} is: {crop_labels[label]}")
        else:
            st.write("Invalid label. Please enter a valid numeric label.")
    except ValueError:
        st.write("Please enter a numeric label.")

    #code for prediction

    Report=''

    #creating a button for prediction

    if st.button('Fertilizer Recommendation Result'):
        Report=fertilizer_prediction([temperature,humidity,ph,rainfall,label])

    st.success(Report)


if __name__ =='__main__':
    main()
    


