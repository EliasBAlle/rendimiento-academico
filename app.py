import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree

st.title('Clasificador de rendimiento estudiantil!')

# Cargar los datos
df = pd.read_csv('Data/student-por.csv', sep=';')

# Crear una nueva columna de rendimiento basado en G3
df['performance'] = pd.cut(df['G3'], bins=[0, 4, 8, 12, 16, 20], labels=['Muy bajo', 'Malo', 'Regular', 'Alto', 'Excelente'])

# Seleccionar las características y etiquetas
features = ['G1', 'G2', 'studytime', 'failures', 'absences', 'Medu', 'Fedu', 'schoolsup', 'higher', 'goout']
X = df[features]
y = df['performance']
y_reg = df['G3']

# Codificar variables categóricas
X = pd.get_dummies(X, columns=['schoolsup', 'higher'], drop_first=True)

# Manejar valores NaN en X (rellenar con la media de la columna)
X.fillna(X.mean(), inplace=True)

# Manejar valores NaN en y y y_reg (eliminar filas con NaN en y o y_reg)
X = X[y.notna() & y_reg.notna()]
y = y[y.notna() & y_reg.notna()]
y_reg = y_reg[y.notna() & y_reg.notna()]

# Dividir los datos en entrenamiento y prueba para clasificación
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Dividir los datos en entrenamiento y prueba para regresión
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2)

# Crear y entrenar el modelo de clasificación
modelo_arbol_c = tree.DecisionTreeClassifier()
modelo_arbol_c = modelo_arbol_c.fit(X_train, y_train)

# Crear y entrenar el modelo de regresión para predecir G3
modelo_arbol_r = tree.DecisionTreeRegressor()
modelo_arbol_r = modelo_arbol_r.fit(X_train_reg, y_train_reg)

# Crear la interfaz de Streamlit
with st.sidebar:
    st.sidebar.subheader('Parámetros')
    G1 = st.slider('Nota del primer corte', 0.0, 5.0)
    G2 = st.slider('Nota del segundo corte', 0.0, 5.0)
    studytime = st.slider('Tiempo de estudio semanal', float(df['studytime'].min()), float(df['studytime'].max()))
    failures = st.slider('Número de fracasos de clases anteriores', float(df['failures'].min()), float(df['failures'].max()))
    absences = st.slider('Número de ausencias escolares', float(df['absences'].min()), float(df['absences'].max()))
    Medu = st.slider('Educación de la madre', float(df['Medu'].min()), float(df['Medu'].max()))
    Fedu = st.slider('Educación del padre', float(df['Fedu'].min()), float(df['Fedu'].max()))
    schoolsup = st.selectbox('Apoyo educativo adicional', df['schoolsup'].unique())
    higher = st.selectbox('Desea cursar educación superior', df['higher'].unique())
    goout = st.slider('Salidas con amigos', float(df['goout'].min()), float(df['goout'].max()))

# Predecir con el modelo
entrada = pd.DataFrame([[G1*4, G2*4, studytime, failures, absences, Medu, Fedu, schoolsup, higher, goout]], columns=features)

# Codificar la entrada de usuario de la misma manera que los datos de entrenamiento
entrada = pd.get_dummies(entrada, columns=['schoolsup', 'higher'], drop_first=True)

# Asegurarse de que las columnas de entrada coincidan con las del entrenamiento
entrada = entrada.reindex(columns=X_train.columns, fill_value=0)

# Predecir el resultado de rendimiento
resultado = modelo_arbol_c.predict(entrada)
st.write('El resultado es:', resultado[0])

# Predecir la nota final aproximada
prediccion_G3 = modelo_arbol_r.predict(entrada)
nota_final_aproximada = prediccion_G3[0] / 4
nota_final = round(nota_final_aproximada, 2)
st.write('La nota final aproximada está entre:', nota_final - 0.25, 'y', nota_final + 0.25)

st.write('Porcentaje de acierto:', modelo_arbol_c.score(X_test, y_test) * 100, '%')
st.write('Porcentaje de acierto de regresión:', modelo_arbol_r.score(X_test_reg, y_test_reg) * 100, '%')

# Mostrar imagen según el resultado (opcional)
if resultado[0] == 'Muy bajo':
    st.image('https://image.isu.pub/211120003018-85a8f6801dbe35c5745c79f0dfe5f2f6/jpg/page_1_thumb_large.jpg', width=600)
elif resultado[0] == 'Malo':
    st.image('https://www.sabermas.umich.mx/images/stories/64/ARTICULO2A1.png', width=600)
elif resultado[0] == 'Regular':
    st.image('https://via.placeholder.com/600x400.png?text=Regular+rendimiento', width=600)
elif resultado[0] == 'Alto':
    st.image('https://via.placeholder.com/600x400.png?text=Alto+rendimiento', width=600)
else:
    st.image('https://via.placeholder.com/600x400.png?text=Excelente', width=600)

# Identificar parámetros que influyen en bajo rendimiento
if resultado[0] in ['Muy bajo', 'Malo']:
    st.write("## Recomendaciones para mejorar el rendimiento")
    if G1 < 10:
        st.write("Recomendación: Mejora en la nota del primer corte. Considere aumentar el tiempo de estudio y buscar ayuda adicional.")
    if G2 < 10:
        st.write("Recomendación: Mejora en la nota del segundo corte. Considere participar en tutorías y grupos de estudio.")
    if studytime < 2:
        st.write("Recomendación: Aumentar el tiempo de estudio semanal. Intente organizar un horario de estudio regular.")
    if failures > 0:
        st.write("Recomendación: Reducir el número de fracasos en clases anteriores. Trabaje en técnicas de estudio más efectivas y pida apoyo.")
    if absences > 5:
        st.write("Recomendación: Reducir el número de ausencias escolares. Asistir a clases regularmente es crucial para el éxito académico.")
    if Medu < 2:
        st.write("Recomendación: Considerar involucrar más a la madre en el proceso educativo.")
    if Fedu < 2:
        st.write("Recomendación: Considerar involucrar más al padre en el proceso educativo.")
    if schoolsup == 'no':
        st.write("Recomendación: Solicitar apoyo educativo adicional si está disponible.")
    if higher == 'no':
        st.write("Recomendación: Reflexionar sobre la importancia de la educación superior y buscar orientación vocacional.")
    if goout > 3:
        st.write("Recomendación: Reducir las salidas con amigos y enfocarse más en los estudios.")
