import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.title('Predictor de Admisión a la Universidad')

# Cargar los datos
df = pd.read_csv('Data/Admission_Predict.csv')

# Seleccionar las características y etiquetas
features = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']
X = df[features]
y = df['Chance of Admit ']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Crear la interfaz de Streamlit
st.sidebar.subheader('Parámetros de Entrada')
GRE_Score = st.sidebar.slider('Prueba de examen de registros de postgrados',260,340 , int(df['GRE Score'].mean()))
TOEFL_Score = st.sidebar.slider('Prueba de ingles como lengua extrangera (TOEFL)',0,120, int(df['TOEFL Score'].mean()))
University_Rating = st.sidebar.slider('Calificacion de la universidad', int(df['University Rating'].min()), int(df['University Rating'].max()), int(df['University Rating'].mean()))
SOP = st.sidebar.slider('Declaracion de Proposito ', float(df['SOP'].min()), float(df['SOP'].max()), float(df['SOP'].mean()))
LOR = st.sidebar.slider('Carta de recomendacion', float(df['LOR '].min()), float(df['LOR '].max()), float(df['LOR '].mean()))
CGPA = st.sidebar.slider('Promedio acumulado de calificaciones',0.0,10.0, float(df['CGPA'].mean()))
Research = st.sidebar.selectbox('Experiencia de investigacion', [0, 1])

# Crear entrada del usuario
entrada = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]], columns=features)

# Predecir la probabilidad de admisión
probabilidad_admision = modelo.predict(entrada)[0]
st.write('La probabilidad de admisión es:', round(probabilidad_admision, 2))

# Mostrar métricas de rendimiento
st.write('MSE del modelo:', mse)
st.write('Coeficiente de Determinación del modelo:', r2)
