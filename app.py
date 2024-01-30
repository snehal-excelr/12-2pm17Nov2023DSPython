# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:30:25 2023

@author: excel
"""

import pickle
import streamlit as st

load = open('clf.pkl','rb')
model = pickle.load(load)


    
def predict(preg,plas,pres,skin,test,mass,pedi,age):
    prediction = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    return prediction
def main():
    st.title('Pima Indian Diabetese')
    
    preg = st.number_input('Pregnancy: ')
    plas = st.number_input('Plasma: ')    
    pres = st.number_input('Pres: ')
    skin = st.number_input('Skin: ')
    test = st.number_input('Test: ')
    mass = st.number_input('Mass: ')
    pedi = st.number_input('Pedigree: ')
    age = st.number_input('Age: ')

#    if st.button('Predict'):
#        result = predict(preg,plas,pres,skin,test,mass,pedi,age)
#        st.success('Diabetic:  {} '.format(result))

    if st.button('Predict'):
         result = predict(preg,plas,pres,skin,test,mass,pedi,age)
         if result==0:
             st.success("Non-Diabetic Person")
         else:
             st.success("Diabetic Person")


        
if __name__ == '__main__':
    main()
        
        

        
        
        
        
        
        
        