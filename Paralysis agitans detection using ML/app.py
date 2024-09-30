import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Parkinson Disease Prediction System',
                           [
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)(80 to 300)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)(150 to 600)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)(80 to 250)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)(0 to 1)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)(0 to 1)')

    with col1:
        RAP = st.text_input('MDVP:RAP(0 to 1)')

    with col2:
        PPQ = st.text_input('MDVP:PPQ(0 to 1)')

    with col3:
        DDP = st.text_input('Jitter:DDP(0 to 1)')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer(0 to 1)')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)(0 to 1)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3(0 to 1)')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5(0 to 1)')

    with col3:
        APQ = st.text_input('MDVP:APQ(0 to 1)')

    with col4:
        DDA = st.text_input('Shimmer:DDA(0 to 1)')

    with col5:
        NHR = st.text_input('NHR(0 to 1)')

    with col1:
        HNR = st.text_input('HNR(5 to 30)')

    with col2:
        HNR = st.text_input('status(0 and 1)') 

    with col3:
        RPDE = st.text_input('RPDE(0 to 1)')

    with col4:
        DFA = st.text_input('DFA(0 to 1)')

    with col5:
        spread1 = st.text_input('spread1(-7 to 0)')

    with col1:
        spread2 = st.text_input('spread2(0 to 1)')

    with col2:
        D2 = st.text_input('D2(1 to 3)')

    with col3:
        PPE = st.text_input('PPE(0 to 1)')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
