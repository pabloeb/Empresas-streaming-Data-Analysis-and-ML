# Proyecto-ML-Labs1



![logos](https://i0.wp.com/revistapuntobo.com/wp-content/uploads/2020/09/netflix-disney-plus-amazon-hulu-1205084-1280x0-1.jpeg)



`Entorno:`  
El presente repositorio contiene un proyecto que forma parte del entrenamiento en Ciencia de Datos de la etapa de proyectos de la   
academia Henry.  

`Objetivos:`  
Por un lado, a través de varios datasets de usuarios que contienen los datos de usuarios y películas de empresas renombradas de streaming,  
se elabora una API con FASTAPI que consume los datos de un dataframe unificado y responde consultas en base a los requerimientos solicitados.
Las consultas son:  

- Consulta 1:  
Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse  
get_max_duration(year, platform, duration_type))

- Consulta 2:  
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse   
get_score_count(platform, scored, year)) 

- Consulta 3:  
Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))  

Por otro lado, a través de un algoritmo de Machine Learning del tipo Sistema de Recomendación basado en la técnica  
de filtro colaborativo, se busca predecir si una película determinada es recomendable para un usuario dado.


`FastAPI en Render`

Se puede acceder a la consola de FastAPI a través del siguiente enlace:  

https://proyecto-ml-labs1-09ll.onrender.com

Se ingresa a una imagen de portada y luego haciendo click sobre la pantalla se redirige a /docs donde se realizan la    
mencionadas consultas. Los parámetros correspondientes son los siguientes:  

- Parametros consulta1 : year (número entero entre 1920 y 2021),platform (Netflix,Hulu,Disney,Amazon), duration_type (min, season)  

- Parametros consulta2 : year (número entero entre 1920 y 2021),platform (Netflix,Hulu,Disney,Amazon), scored (0 a 5 con intervalos de 0.5))  

- Parametros consulta3 : platform (Netflix,Hulu,Disney,Amazon)  

Tambien se puede hacer consultas directamente a través de la URL, por ejemplo:   

https://proyecto-ml-labs1-09ll.onrender.com/consulta1?year=2014&platform=Netflix&duration_type=min 


`Consola de Gradio para predicciones de ML`  

Se puede ingresar a la consola a través del siguiente enlace:  

https://7f9e3f7e0c4f7b7f12.gradio.live

Se debe ingresar un número de identificación de cliente y de película. El modelo responderá el valor que ese usuario asignaría a la  
película y en función de ello, si se le recomienda o no.El valor fijado para recomendar las películases de 3.75 puntos o más sobre un  
máximo de 5.

`Otro contenido del repositorio`
Hay una serie de archivos para revisar el código utilizado para construir el proyecto.  

main.py : contiene el código para creación de la API  

Consola Gradio.ipynb : contiene el código para creación de la consola de Gradio  

EDA_Sistema_Recomendacion.ipynb: contiene el codigo del EDA y del modelo de Machine Learning (SVD,KNNWithMEANS,NMF)  

ETA_inicio_proyecto.ipynb: contiene la fase inicial del proyecto , limpieza y ordenamiento de datos.



