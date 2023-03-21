# Proyecto-ML-Labs1
# proyecto-labs-ML


![logos](https://i0.wp.com/revistapuntobo.com/wp-content/uploads/2020/09/netflix-disney-plus-amazon-hulu-1205084-1280x0-1.jpeg)



`Entorno:`  
El presente repositorio contiene un proyecto que forma parte del entrenamiento en Ciencia de Datos de la etapa de proyectos de la   
academia Henry.  

`Objetivo:`  
A través de varios datasets de usuarios y de contenido de empresas renombradas de streaming, se elabora una API con FASTAPI que   
consume los datos de de un dataframe unificado y responde consultas relativas a la temática establecida, en base a requerimientos  
solicitados, que emulan el posible interés de un usuario general promedio:
Las consultas son:  

- Consulta 1:  
Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse  
get_max_duration(year, platform, duration_type))

- Consulta 2:  
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse   
get_score_count(platform, scored, year)) 

- Consulta 3:  
Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))


``` fix
El proyecto consta de dos alternativas.  
- Clonar el repositorio y correr un servidor local con uvicorn desde el localhost o,  
- Hacer las consultas a través de la API deployada en el host Render a través de un enlace de internet.  
```


 ### VERSION LOCAL

`Instalación:`
- Para instalar las dependencias necesarias para la API, se recomienda utilizar un entorno virtual de Python.  
- Una vez instalado y activado el entorno virtual, instalar las dependencias del archivo .txt (sólo fastapi, pandas,uvicorn,  
 typing,numpy)
 
`Uso:`  
Para ejecutar la API, ejecutar el siguiente comando en la consola en la raiz del proyecto:   

**uvicorn main:app --reload**  

Esto iniciará el servidor y se podrá acceder a la API en la dirección http://localhost:8000/docs.

`Consulta:`  

La consulta se realiza mediante el endpoint: **/consultax**  

donde **x** debe ser reemplzado por los números(1,2,3) de acuerdo a lo expuesto en el apartado **Objetivos**   
Todos los parámetros para filtrar la respuesta son OPTATIVOS.

Parametros consulta1 : year (número entero entre 1920 y 2021),platform (Netflix,Hulu,Disney,Amazon), duration_type (min, season)  
Parametros consulta2 : year (número entero entre 1920 y 2021),platform (Netflix,Hulu,Disney,Amazon), scored (0 a 5 con intervalos de 0.5))  
Parametros consulta3 : platform (Netflix,Hulu,Disney,Amazon)  

Por ejemplo, para buscar la película más larga del año 2014 en Netflix, hay que colocar en el nvegador:

`http://localhost:8000/consulta1?year=2014&platform=Netflix&duration_type=min   


`Respuesta`  

La respuesta de la API es en formato str:

`"La pelicula de mayor duración es The Gospel of Matthew con 190 min"`  
  
  

### VERSION WEB HOSTEADA EN RENDER:  

A través de siguiente link https://proyecto-sreaming-queries.onrender.com se puede acceder a la API directamente en el browser.  

En lapantalla inicial , se presiona el botón con el link para iniciar las consultas. 





Consola de Fastapi en Render:
https://proyecto-ml-labs1-09ll.onrender.com



consola de Gradio:
https://4733be70282cf851ac.gradio.live
