#Importing Libraries
#!pip install python-Levenshtein
import Levenshtein

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import textwrap

#List of the symptoms is listed here in list l1.

l1=['back pain','constipation','abdominal pain','diarrhoea','mild fever','yellow urine',
    'yellowing of eyes','acute liver failure','fluid overload','swelling of stomach',
    'swelled lymph nodes','malaise','blurred and distorted vision','phlegm','throat irritation',
    'redness of eyes','sinus pressure','runny nose','congestion','chest pain','weakness in limbs',
    'fast heart rate','pain during bowel movements','pain in anal region','bloody stool',
    'irritation in anus','neck pain','dizziness','cramps','bruising','obesity','swollen legs',
    'swollen blood vessels','puffy face and eyes', 'headache',
    'excessive hunger','drying and tingling lips', 'cough',
    'slurred speech','knee pain','hip joint pain','muscle weakness','stiff neck','swelling joints',
    'movement stiffness','spinning movements','loss of balance','unsteadiness',
    'weakness of one body side','loss of smell','bladder discomfort','foul smell of urine',
    'depression','irritability','muscle pain','altered sensorium','red spots over body','belly pain',
    'abnormal menstruation','dischromic  patches','watery eyes','increased appetite','polyuria','mucoid sputum',
    'rusty sputum','lack of concentration','receiving blood transfusion',
    'coma','stomach bleeding','distention of abdomen',
    'history of alcohol consumption','fluid overload','blood in sputum','prominent veins on calf',
    'palpitations','painful walking','pus filled pimples','blackheads','scurring','skin peeling',
    'silver like dusting','small dents in nails','inflammatory nails','blister','red sore around nose',
    'yellow crust ooze', 'itching', 'skin rash', 'shivering', 'chills', 'fatigue'
]

#List of Diseases is listed in list disease.

disease=['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
       'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
       'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',
       'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
       'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
       'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
       'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
       'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',
       'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
       'Osteoarthristis', 'Arthritis',
       '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
       'Urinary tract infection', 'Psoriasis', 'Impetigo']

#disease = [df['prognosis'].unique()]
#print(disease)

l2=[]
for i in range(0,len(l1)):
    l2.append(0)

#Reading the training .csv file
df=pd.read_csv("training.csv")
DF= pd.read_csv('training.csv', index_col='prognosis')
#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)
#df.head()
DF.head()

X= df[l1]
y = df[["prognosis"]]
np.ravel(y)

#Reading the  testing.csv file
tr=pd.read_csv("testing.csv")

#Using inbuilt function replace in pandas for replacing the values

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)
tr.head()

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

def find_closest_match(input_text, word_list):
    highest_score = 0
    closest_match = None

    for word in word_list:
        score = Levenshtein.ratio(input_text.lower(), word.lower())

        if score > highest_score:
            highest_score = score
            closest_match = word

    return closest_match

import csv
def map_word_to_row(word):
    with open('symptom_Description.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0] == word:
                return row[0], row[1]

    return None, None  # Word not found

import csv
def map_word_to_rowPrecaution(word):
    with open('symptom_precaution.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0] == word:
                return ' '.join([val.capitalize() for val in row[1:5]])

    return None  # Word not found

#root = Tk()


def randomforest(symptom1):
    clf4 = RandomForestClassifier(n_estimators=100)
    clf4 = clf4.fit(X, np.ravel(y))

    y_train_pred = clf4.predict(X)
    train_accuracy = accuracy_score(y, y_train_pred)
    

    y_pred = clf4.predict(X_test)
    print("Random Forest")
    print("Training Accuracy:", train_accuracy)
    
    psymptoms = []

    for word in l1:
        if word in symptom1:
            psymptoms.append(word)

    print(psymptoms)

    l2 = [0] * len(l1)
    check = 0
    for k in range(len(l1)):
        if l1[k] in psymptoms:
            l2[k] = 1
            check = 1
    
    if check == 0:
        return "Provide a valid symptoms."

    inputtest = [l2]
    predictions = clf4.predict_proba(inputtest)
    predicted_labels = []
    for prediction in predictions:
        top_3_indices = np.argsort(prediction)[-3:][::-1]  # Get the indices of top 3 probabilities
        top_3_labels = [disease[index] for index in top_3_indices]
        predicted_labels.append(top_3_labels)

    print(predicted_labels)
    if predicted_labels:
        formatted_outputs = []
        for labels in predicted_labels:
            output_lines = []
            i = 1
            for label in labels:
                disease_description = map_word_to_row(label)[1]
                precaution = map_word_to_rowPrecaution(label)
                output_lines.append(f"{i}. <b>{label}</b>: {disease_description}\nPrecaution: {precaution}")
                i+=1
            formatted_output = "\n\n".join(output_lines)
            formatted_outputs.append(formatted_output)
            print(formatted_output)
        return formatted_output
    else:
        print("Not Found")
        return "Not Found"

