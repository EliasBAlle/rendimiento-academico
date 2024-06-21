# rendimiento-academico


**Contexto:** En una institución educativa, se ha observado una variabilidad significativa en el rendimiento estudiantil a lo largo de los años. La administración escolar está interesada en identificar factores que puedan influir en el rendimiento para implementar estrategias de apoyo personalizadas.


**Problemática:** Se necesita un sistema que permita predecir el rendimiento estudiantil basado en datos históricos y factores personales, académicos y sociales. El objetivo es identificar a los estudiantes que podrían estar en riesgo de bajo rendimiento para proporcionarles recursos adicionales y apoyo a tiempo.


**Aplicación del modelo:** El modelo de clasificación de rendimiento estudiantil creado podría aplicarse para analizar los datos de los estudiantes actuales y predecir su categoría de rendimiento (‘Bajo’, ‘Medio’, ‘Alto’). Con esta información, la institución podría intervenir temprano con los estudiantes predichos como de bajo rendimiento, ofreciendo tutorías, asesoramiento académico, o servicios de apoyo emocional y social.

Información sobre el conjunto de datos:

school - Escuela del estudiante (binario: 'GP' - Gabriel Pereira o 'MS' - Mousinho da Silveira)


sex - Sexo del estudiante (binario: 'F' - mujer o 'M' - hombre)


age - Edad del estudiante (numérica: de 15 a 22)


address - Tipo de dirección del hogar del estudiante (binario: 'U' - urbano o 'R' - rural)


famsize - Tamaño de la familia (binario: 'LE3' - menor o igual a 3 o 'GT3' - mayor que 3)


Pstatus - Estado de convivencia de los padres (binario: 'T' - vivir juntos o 'A' - aparte)


Medu - Educación de la madre (numérico: 0 - ninguno, 1 - educación primaria (4º grado), 2 - 5º a 9º grado, 3 - educación secundaria, 4 - educación superior)


Fedu - Educación del padre (numérico: 0 - ninguno, 1 - educación primaria (4º grado), 2º - 5º a 9º grado, 3º - educación secundaria, 4º - educación superior)


Mjob- Trabajo de la madre (nominal: 'maestro', 'salud' relacionado, 'servicios' civiles (por ejemplo, administrativo o policial), 'at_home' u 'otro')


Fjob - Trabajo del padre (nominal: 'maestro', 'salud' relacionado, 'servicios' civiles (por ejemplo, administrativo o policial), 'at_home' u 'otro')


reason - Razón para elegir esta escuela (nominal: cerca de 'casa', 'reputación' de la escuela, preferencia de 'curso' u 'otro')


guardian - Tutor del estudiante (nominal: 'madre', 'padre' u 'otro')


traveltime - Tiempo de viaje de casa a la escuela (numérico: 1 - < 15 min., 2 - 15 a 30 min., 3 - 30 min. a 1 hora, o 4 - >1 hora)


studytime - Tiempo de estudio semanal (numérico: 1 - < 2 horas, 2 - 2 a 5 horas, 3 - 5 a 10 horas, o 4 - >10 horas)


failures - Número de fracasos de clases anteriores (numérico: n si 1< = n < 3, de lo contrario 4)


schoolsup - Apoyo educativo adicional (binario: sí o no)


famsup - Apoyo educativo familiar (binario: sí o no)


paid - Clases extra pagadas dentro de la asignatura del curso (Matemáticas o Portugués) (binario: sí o no)


activities - Actividades extracurriculares (binario: sí o no)


nursery - Asistió a la guardería (binario: sí o no)


higher - Quiere tomar educación superior (binario: sí o no)


internet - Acceso a Internet en casa (binario: sí o no)


romantic - Con una relación romántica (binario: sí o no)


famrel - Calidad de las relaciones familiares (numérica: de 1 - muy malo a 5 - excelente)


freetime - Tiempo libre después de la escuela (numérico: de 1 - muy bajo a 5 - muy alto)


goout (numérico: de 1 - muy bajo a 5 - muy alto)


Dalc - Consumo de alcohol en la jornada laboral (numérico: de 1 - muy bajo a 5 - muy alto)



Walc - Consumo de alcohol de fin de semana (numérico: de 1 - muy bajo a 5 - muy alto)


health - Estado de salud actual (numérico: de 1 - muy malo a 5 - muy bueno)


absences - Número de ausencias escolares (numérico: de 0 a 93)


Los siguientes grados están relacionados con la asignatura del curso, Matemáticas o Portugués:


31. G1 - Nota del Primer corte (numérico: de 0 a 20)


31. G2 - Nota del Segundo corte (numérico: de 0 a 20)


32. G3 - Nota final (numérica: de 0 a 20, objetivo de salida)


