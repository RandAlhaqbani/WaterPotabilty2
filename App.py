from sklearn.svm import SVC
import streamlit as st
import pickle 

knn=pickle.load(open('svc_classifier.pkl','rb'))

def classify(num):
    if num==0:
        return 'Not Potable'
    
    else:
        return 'Potable'
    

def main():
 
 st.title('Thank you !')
#title
st.title('Water Potability')

st.header('about the web')
st.write(' This website helps you determine if your water is safe to drink! Enter details about your water source, and well analyze it based on known contaminants and provide a preliminary assessment of its potability.')
st.write('Unquench your thirst for uncertainty! This website takes the guesswork out of water safety.  In seconds, our cutting-edge technology analyzes your water source and delivers a clear answer: safe to sip or skip.  Enjoy peace of mind with every gulp - hydrate confidently, knowing your H2O is good to go.')

st.subheader('Enter the total ph of your water:') 
ph =st.number_input('Enter the Ph of your water (number):') 
st.write(' The water Ph you have entered is :' , ph)


st.subheader('Enter the Hardness in the water:')    
Hardness =st.number_input('Enter the hardness of the water (number):')
st.write(' The Hardness that you entered :' , Hardness)

 
st.subheader('Enter the total dissolved solids in the water:') 
Solids =st.number_input(' Enter the solids of the water:') 
st.write(' The number of total dissolved solids you entered :' , Solids)


st.subheader('Enter the chloramines number:')
Chloramines =st.number_input(' Enter the chloramines of the water:')
st.write(' The number of  chloramines you entered :' , Chloramines)

st.subheader('Enter the sulfate number:')
Sulfate =st.number_input(' Enter the sulfate of the water:')
st.write(' The number of  sulfate you entered :' , Sulfate)


st.subheader('Enter the amount of conductivity:')
Conductivity =st.number_input(' Enter the amount of conductivity:')
st.write(' The amount of conductivity you entered :' , Conductivity)


st.subheader('Enter the amount of organic carbon:')
Organic_carbon =st.number_input('Enter the amount of organic carbon (number):')
st.write(' The amount of organic carbon you entered :' , Organic_carbon)


st.subheader('Enter the amount of trihalomethanes:')
Trihalomethanes =st.number_input('Enter the amount of trihalomethanes:')
st.write(' The amount of trihalomethanes you entered :' , Trihalomethanes)


st.subheader('Enter the amount of turbidity:')
Turbidity =st.number_input(' Enter the amount of turbidity:')
st.write(' The amount of turbidity you entered :' , Turbidity)

st.balloons()


inputs = [[ph,Hardness, Solids, Chloramines,Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]]
if st.button('classify'):
     st.success(classify(SVC.predict(inputs)))



if __name__=='__main__':
    main()