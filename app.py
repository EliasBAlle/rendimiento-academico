import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree

st.title('Clasificador de rendimiento estudiantil!')

# Cargar los datos
df = pd.read_csv('Data/student-por.csv', sep=';')

# Crear una nueva columna de rendimiento basado en G3
df['performance'] = pd.cut(df['G3'], bins=[0, 10, 15, 20], labels=['Bajo', 'Medio', 'Alto'])

# Seleccionar las características y etiquetas
features = ['G1', 'G2', 'studytime', 'failures', 'absences', 'famsup', 'schoolsup', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']
X = df[features]
y = df['performance']

# Codificar variables categóricas
X = pd.get_dummies(X, columns=['famsup', 'schoolsup', 'higher', 'internet', 'romantic'], drop_first=True)

# Manejar valores NaN en X (rellenar con la media de la columna)
X.fillna(X.mean(), inplace=True)

# Manejar valores NaN en y (eliminar filas con NaN en y)
X = X[y.notna()]
y = y.dropna()
# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear y entrenar el modelo
modelo_arbol_c = tree.DecisionTreeClassifier()
modelo_arbol_c = modelo_arbol_c.fit(X_train, y_train)

# Crear la interfaz de Streamlit
with st.sidebar:
    st.sidebar.subheader('Parámetros')
    G1 = st.slider('nota primer corte',0.0,5.0)
    G2 = st.slider('nota segundo corte',0.0,5.0)
    studytime = st.slider('Horas de estudio por semana', float(df['studytime'].min()), float(df['studytime'].max()))
    failures = st.slider('Número de fracasos', float(df['failures'].min()), float(df['failures'].max()))
    absences = st.slider('Número de ausencias', float(df['absences'].min()), float(df['absences'].max()))
    famsup = st.selectbox('Apoyo familiar', df['famsup'].unique())
    schoolsup = st.selectbox('Apoyo escolar', df['schoolsup'].unique())
    higher = st.selectbox('Desea educación superior', df['higher'].unique())
    internet = st.selectbox('Acceso a internet en casa', df['internet'].unique())
    romantic = st.selectbox('Relación romántica', df['romantic'].unique())
    famrel = st.slider('Relaciones familiares', float(df['famrel'].min()), float(df['famrel'].max()))
    freetime = st.slider('Tiempo libre', float(df['freetime'].min()), float(df['freetime'].max()))
    goout = st.slider('Salir con amigos', float(df['goout'].min()), float(df['goout'].max()))
    Dalc = st.slider('Consumo de alcohol entre semana', float(df['Dalc'].min()), float(df['Dalc'].max()))
    Walc = st.slider('Consumo de alcohol en el fin de semana', float(df['Walc'].min()), float(df['Walc'].max()))
    health = st.slider('Estado de salud', float(df['health'].min()), float(df['health'].max()))

# Predecir con el modelo
entrada = pd.DataFrame([[G1, G2, studytime, failures, absences, famsup, schoolsup, higher, internet, romantic, famrel, freetime, goout, Dalc, Walc, health]], columns=features)

# Codificar la entrada de usuario de la misma manera que los datos de entrenamiento
entrada = pd.get_dummies(entrada, columns=['famsup', 'schoolsup', 'higher', 'internet', 'romantic'], drop_first=True)

# Asegurarse de que las columnas de entrada coincidan con las del entrenamiento
entrada = entrada.reindex(columns=X_train.columns, fill_value=0)

# Predecir el resultado
resultado = modelo_arbol_c.predict(entrada)
st.write('El resultado es:', resultado[0])
st.write('Porcentaje de acierto:', modelo_arbol_c.score(X_test, y_test) * 100, '%')

# Mostrar imagen según el resultado (opcional)
if resultado[0] == 'Bajo':
    st.image('https://image.isu.pub/211120003018-85a8f6801dbe35c5745c79f0dfe5f2f6/jpg/page_1_thumb_large.jpg', width=600)
elif resultado[0] == 'Medio':
    st.image('https://via.placeholder.com/600x400.png?text=Medio+rendimiento', width=600)
else:
    st.image('https://via.placeholder.com/600x400.png?text=Alto+rendimiento', width=600)
