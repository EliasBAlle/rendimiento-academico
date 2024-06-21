import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree

st.title('Clasificador de rendimiento estudiantil!')

# Cargar los datos
df = pd.read_csv('Data/student-data.csv', sep=',')

# Verificar las columnas presentes en el DataFrame
st.write("Columnas disponibles en el dataset:", df.columns.tolist())

# Asegurarse de que 'passed' está presente
if 'passed' not in df.columns:
    st.error("La columna 'passed' no está presente en el dataset. Asegúrate de que el dataset es correcto.")
else:
    # Utilizar 'passed' como etiqueta de destino
    df['performance'] = df['passed']

    # Seleccionar las características y etiquetas
    features = [
        'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob',
        'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid',
        'activities', 'higher', 'internet', 'famrel', 'freetime', 'goout',
        'Dalc', 'Walc', 'health', 'absences'
    ]
    X = df[features]
    y = df['performance']

    # Codificar variables categóricas
    X = pd.get_dummies(X, drop_first=True)

    # Manejar valores NaN (rellenar con la media de la columna)
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
        age = st.slider('Edad', int(df['age'].min()), int(df['age'].max()))
        address = st.selectbox('Dirección', df['address'].unique())
        famsize = st.selectbox('Tamaño de la familia', df['famsize'].unique())
        Pstatus = st.selectbox('Estado de convivencia de los padres', df['Pstatus'].unique())
        Medu = st.slider('Educación de la madre', int(df['Medu'].min()), int(df['Medu'].max()))
        Fedu = st.slider('Educación del padre', int(df['Fedu'].min()), int(df['Fedu'].max()))
        Mjob = st.selectbox('Trabajo de la madre', df['Mjob'].unique())
        Fjob = st.selectbox('Trabajo del padre', df['Fjob'].unique())
        traveltime = st.slider('Tiempo de viaje a la escuela', int(df['traveltime'].min()), int(df['traveltime'].max()))
        studytime = st.slider('Tiempo de estudio semanal', int(df['studytime'].min()), int(df['studytime'].max()))
        failures = st.slider('Número de fracasos', int(df['failures'].min()), int(df['failures'].max()))
        schoolsup = st.selectbox('Apoyo educativo adicional', df['schoolsup'].unique())
        famsup = st.selectbox('Apoyo educativo familiar', df['famsup'].unique())
        paid = st.selectbox('Clases extra pagadas', df['paid'].unique())
        activities = st.selectbox('Actividades extracurriculares', df['activities'].unique())
        higher = st.selectbox('Desea educación superior', df['higher'].unique())
        internet = st.selectbox('Acceso a internet en casa', df['internet'].unique())
        famrel = st.slider('Relaciones familiares', int(df['famrel'].min()), int(df['famrel'].max()))
        freetime = st.slider('Tiempo libre', int(df['freetime'].min()), int(df['freetime'].max()))
        goout = st.slider('Salir con amigos', int(df['goout'].min()), int(df['goout'].max()))
        Dalc = st.slider('Consumo de alcohol en jornada laboral', int(df['Dalc'].min()), int(df['Dalc'].max()))
        Walc = st.slider('Consumo de alcohol en el fin de semana', int(df['Walc'].min()), int(df['Walc'].max()))
        health = st.slider('Estado de salud', int(df['health'].min()), int(df['health'].max()))
        absences = st.slider('Número de ausencias', int(df['absences'].min()), int(df['absences'].max()))

    # Predecir con el modelo
    entrada = pd.DataFrame([[
        age, address, famsize, Pstatus, Medu, Fedu, Mjob, Fjob,
        traveltime, studytime, failures, schoolsup, famsup, paid,
        activities, higher, internet, famrel, freetime, goout,
        Dalc, Walc, health, absences
    ]], columns=features)

    # Codificar la entrada de usuario de la misma manera que los datos de entrenamiento
    entrada = pd.get_dummies(entrada, drop_first=True)

    # Asegurarse de que las columnas de entrada coincidan con las del entrenamiento
    entrada = entrada.reindex(columns=X_train.columns, fill_value=0)

    # Predecir el resultado
    resultado = modelo_arbol_c.predict(entrada)
    st.write('El resultado es:', resultado[0])
    st.write('Porcentaje de acierto:', modelo_arbol_c.score(X_test, y_test) * 100, '%')

    # Mostrar imagen según el resultado (opcional)
    if resultado[0] == 'yes':
        st.image('https://via.placeholder.com/600x400.png?text=Pasado', width=600)
    else:
        st.image('https://via.placeholder.com/600x400.png?text=No+Pasado', width=600)
