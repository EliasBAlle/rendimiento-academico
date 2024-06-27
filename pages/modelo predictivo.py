import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Cargar los datos
df = pd.read_excel('../Data/data_academic_performance.csv')
# Mapeo de valores textuales a numéricos
map_values = {
    'Three': 3,
    'Five': 5,
    'One': 1,
    'Four': 4,
    'Six': 6,
    'Two': 2,
    'Twelve or more': 12,
    'Nueve': 9,
    'Eight': 8,
    'Seven': 7,
    'Ten': 10,
    'Once': 11,
    0: 0
}

# Aplicar el mapeo a la columna
df['PEOPLE_HOUSE'] = df['PEOPLE_HOUSE'].map(map_values)

# Verificar que todos los valores ahora son numéricos
print(df['PEOPLE_HOUSE'].unique())

# Seleccionar las características y la etiqueta
features = ['GENDER', 'EDU_FATHER', 'EDU_MOTHER', 'STRATUM', 'PEOPLE_HOUSE', 'CC_PRO', 'ENG_PRO', 'WC_PRO', 'FEP_PRO', 'G_SC']
X = df[features]
y = df['PERCENTILE']

# Codificar variables categóricas
X = pd.get_dummies(X, drop_first=True)

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
gender = st.sidebar.selectbox('Género', df['GENDER'].unique())
edu_father = st.sidebar.selectbox('Educación del Padre', df['EDU_FATHER'].unique())
edu_mother = st.sidebar.selectbox('Educación de la Madre', df['EDU_MOTHER'].unique())
stratum = st.sidebar.selectbox('Estrato', df['STRATUM'].unique())
people_house = st.sidebar.slider('Número de Personas en la Casa', int(df['PEOPLE_HOUSE'].min()), int(df['PEOPLE_HOUSE'].max()), int(df['PEOPLE_HOUSE'].mean()))
cc_pro = st.sidebar.slider('CC_PRO', int(df['CC_PRO'].min()), int(df['CC_PRO'].max()), int(df['CC_PRO'].mean()))
eng_pro = st.sidebar.slider('ENG_PRO', int(df['ENG_PRO'].min()), int(df['ENG_PRO'].max()), int(df['ENG_PRO'].mean()))
wc_pro = st.sidebar.slider('WC_PRO', int(df['WC_PRO'].min()), int(df['WC_PRO'].max()), int(df['WC_PRO'].mean()))
fep_pro = st.sidebar.slider('FEP_PRO', int(df['FEP_PRO'].min()), int(df['FEP_PRO'].max()), int(df['FEP_PRO'].mean()))
g_sc = st.sidebar.slider('G_SC', int(df['G_SC'].min()), int(df['G_SC'].max()), int(df['G_SC'].mean()))

# Crear entrada del usuario
entrada = pd.DataFrame([[gender, edu_father, edu_mother, stratum, people_house, cc_pro, eng_pro, wc_pro, fep_pro, g_sc]], columns=features)

# Codificar la entrada del usuario de la misma manera que los datos de entrenamiento
entrada = pd.get_dummies(entrada, drop_first=True)
entrada = entrada.reindex(columns=X_train.columns, fill_value=0)

# Predecir el percentil del estudiante
percentil_predicho = modelo.predict(entrada)[0]
st.write('El percentil predicho es:', round(percentil_predicho, 2))

# Mostrar métricas de rendimiento
st.write('MSE del modelo:', mse)
st.write('R2 del modelo:', r2)
