import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans

# Create your views here.
def home(request):
    if request.method == 'POST':
        school = request.POST['school']
        department = request.POST['department']
        year = request.POST['year']
        choice = request.POST['choice']

        units_data = pd.read_csv('C:/Users/hellen/Desktop/MY REPOSITORIES/DJANGO-RECOMMENDATION-SYSTEM/UNIT_RECOMMENDATION_SYSTEM/recommendation/data/unit_description.csv')

        vectorizer = TfidfVectorizer(stop_words='english')
        A = vectorizer.fit_transform(units_data['Unit_Description'])
        k=60
        model = KMeans(n_clusters=k, random_state=42).fit(A)
        units_data['cluster'] = model.labels_
        units_data = units_data.set_index('cluster')

        for cluster in range(k):
            all_recommendations = units_data.loc[cluster,['Unit_code','Unit_name', 'Unit_Description']].sample(frac=1).head(10)

        if choice == "" :
            messages.info(request, 'No Input was Provided')
        else:
            net = vectorizer.transform([choice])
            pred = model.predict(net)
            predicted_units = units_data.loc[pred,['Unit_code','Unit_name']].sample(frac=1)
            predicted_units.to_csv('C:/Users/hellen/Desktop/MY REPOSITORIES/DJANGO-RECOMMENDATION-SYSTEM/UNIT_RECOMMENDATION_SYSTEM/recommendation/data/predicted_units.csv')
            csv_predicted = open(f'C:/Users/hellen/Desktop/MY REPOSITORIES/DJANGO-RECOMMENDATION-SYSTEM/UNIT_RECOMMENDATION_SYSTEM/recommendation/data/predicted_units.csv', 'r')
            reader = csv.DictReader(csv_predicted)
            headers = [col for col in reader.fieldnames]
            out = [row for row in reader]
            return render(request, 'rec.html', {'data': out, 'headers':headers})

    return render(request, 'rec.html')



    