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
GRE_Score = st.sidebar.slider('Prueba de examen de registros de postgrados', 260, 340, int(df['GRE Score'].mean()))
TOEFL_Score = st.sidebar.slider('Prueba de inglés como lengua extranjera (TOEFL)', 0, 120, int(df['TOEFL Score'].mean()))
University_Rating = st.sidebar.slider('Calificación de la universidad', int(df['University Rating'].min()), int(df['University Rating'].max()), int(df['University Rating'].mean()))
SOP = st.sidebar.slider('Declaración de Propósito', float(df['SOP'].min()), float(df['SOP'].max()), float(df['SOP'].mean()))
LOR = st.sidebar.slider('Carta de recomendación', float(df['LOR '].min()), float(df['LOR '].max()), float(df['LOR '].mean()))
CGPA = st.sidebar.slider('Promedio acumulado de calificaciones', 0.0, 5.0)
Research = st.sidebar.selectbox('Experiencia de investigación', ['No', 'Sí'])
Research = 1 if Research == 'Sí' else 0

# Crear entrada del usuario
entrada = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA*2, Research]], columns=features)

# Predecir la probabilidad de admisión
probabilidad_admision = max(0, modelo.predict(entrada)[0])
st.write('La probabilidad de admisión es:', round(probabilidad_admision, 2))

# Mostrar métricas de rendimiento
st.write('MSE del modelo:', mse)
st.write('Coeficiente de Determinación del modelo:', r2)

# Recomendaciones si la probabilidad de admisión es menor a 0.6
if probabilidad_admision < 0.6:
    st.write("## Recomendaciones para mejorar la probabilidad de admisión")
    if GRE_Score < 320:
        st.write("Recomendación: Considerar mejorar la puntuación GRE. Practicar más y tomar cursos preparatorios puede ayudar.")
    if TOEFL_Score < 100:
        st.write("Recomendación: Considerar mejorar la puntuación TOEFL. Practicar más y tomar cursos de inglés puede ser beneficioso.")
    if University_Rating < 3:
        st.write("Recomendación: Considerar aplicar a universidades con mejor calificación.")
    if SOP < 4:
        st.write("Recomendación: Mejorar la declaración de propósito. Buscar asesoramiento y revisar varios ejemplos exitosos.")
    if LOR < 4:
        st.write("Recomendación: Obtener cartas de recomendación más fuertes. Pedirlas a profesores o empleadores que te conozcan bien.")
    if CGPA < 3.5:
        st.write("Recomendación: Mejorar el CGPA. Enfocarse en obtener mejores calificaciones en los cursos restantes.")
    if Research == 0:
        st.write("Recomendación: Obtener experiencia en investigación. Participar en proyectos de investigación o trabajos académicos puede ser beneficioso.")
