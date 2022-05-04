import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

#Loading the pickle file with the model
"""
pickle_in = open('unitrecommender.pkl', 'rb') 
recommender = pickle.load(pickle_in)
"""
#Loading unit data of the different schools
units_data = pd.read_csv('data/unit_description.csv')
school_of_computing_data = pd.read_csv('data/school_of_computing.csv') 
school_of_nursing_data = pd.read_csv('data/school_of_nursing.csv')



#Model building
vectorizer = TfidfVectorizer(stop_words='english')
A = vectorizer.fit_transform(units_data['Unit_Description'])
k=60
model = KMeans(n_clusters=k, random_state=42).fit(A)
units_data['cluster'] = model.labels_
units_data = units_data.set_index('cluster')


for cluster in range(k):
    all_recommendations = units_data.loc[cluster,['Unit_code','Unit_name', 'Unit_Description']].sample(frac=1).head(10)


#Working on the display part
st.header('UNIT RECOMMENDER')

school_selectbox = st.selectbox("Select your school",(
    "School of Computing",
    "School of nursing",
))

if school_selectbox == "School of Computing":
    st.selectbox("Select your department",(
        "Information Technology",
        "Computer Science"
    ))


elif school_selectbox == "School of nursing":
    st.selectbox("Select your department",(
        "Nursing",
        "Technology"
    ))

st.selectbox("Select your year of Study",(
    "Year 1",
    "Year 2",
    "Year 3",
    "Year 4"
))
search_text = st.text_input("Choice")

recommend_button = st.button('RECOMMEND')

#Functionality
if recommend_button:
    if search_text == "" :
        st.write("No input")
    else:
        net = vectorizer.transform([search_text])
        pred = model.predict(net)
        predicted_units = units_data.loc[pred,['Unit_code','Unit_name']].sample(frac=1)
        st.write(predicted_units)


