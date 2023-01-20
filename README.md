# <h1 align=center> ** Proyecto Individual Nro.1 - DATA06 ** </h1>
# <h1 align=center>**`Data Engineering`**</h1> 

# <h1 align=center> Mateo Murillo </h1>

![img1](https://user-images.githubusercontent.com/111402986/213601046-e633611a-66cf-404a-aa78-35dd23a7f65b.png)
 
<h1 align=center> ¡Bienvenidos al primer proyecto individual de la etapa de labs! </h1>

## **Introducción**

Para comenzar, quisiera comentarles que durante el desarrollo del primer proyecto tuve que desempeñarme como ***`Data Engineer`*** para una empresa que me solitó ciertos requerimientos para el desarrollo de sus posteriores actividades. A grandes rasgos, debia realizar actividades de extracción, transformación, y carga de datos con el objetivo de disponibilizarlos para desarrollar una Api y ponerla en servicio posterior a su deployment como aplicación web en ***`DETA`***

<p align="center">
<img src = 'https://user-images.githubusercontent.com/111015749/206627044-8b1d9613-0800-4597-869e-1baad4b32172.png' height=250><p>
  
## **ETL**
<i>(Los procesos mostrados a continuación fueron realizados en Python y en su mayoria, utilizando 2 de sus principales librerias para data, Pandas y Numpy).</i>

El primer reto del proyecto consistia en que satisfacer los requerimientos del analista de datos de la empresa. Para ello, contaba con datos provenientes de archivos csv, los cuales debia de limpiar en algunos casos, normalizarlos y realizar algunas otras transformaciones, especificamente las siguentes:

  * Generar una columna **`id`** basandome en la primera letra del nombre de la plataforma de donde provenian estos datos y adjuntandola a los valores de 'show_id' presentes originariamente en los datasets:
  
![image](https://user-images.githubusercontent.com/111402986/213603764-51df96b8-72a7-425c-af55-90ea7b4d3e32.png)
  
<i>(La logica de este mismo codigo lo use para los otros 3 dataset, mi intención era practicar los for en dataframes. Como veran mas adelante, tambien realicé funciones para otro tipo de transformaciones).</i>
  
 * Reemplazar los valores nulos (NaN) de la columna **`rating`** por el string **`g`**(General for all audiences):
  
  ![image](https://user-images.githubusercontent.com/111402986/213605186-06adb764-f067-4e23-904b-16d183c77b91.png)
  
 * Las fechas debia disponerlas con el formato **`AAAA-mm-dd`** :
  
  ![image](https://user-images.githubusercontent.com/111402986/213605496-d5ca89fc-0d9e-4154-88b5-08302f239511.png)
  
 * Todos los campos de texto debia dejarlos en **minúsculas** con el objetivo de normalizarlos:
  
  ![image](https://user-images.githubusercontent.com/111402986/213605879-7d772d8b-0e2b-445c-8940-93a679cf5aa2.png)
 
 * Finalmente debia de integrar dos columnas adicionales: **`duration_int`** (**`rating`**) y **`duration_type`** (***string***), las cuales estaban basadas en el campo **`duration`** :
  
  ![image](https://user-images.githubusercontent.com/111402986/213606418-358bdeea-e4e6-4714-ad39-2cdeab1db3b1.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213606492-1573d498-935c-4167-b82a-ab4874acfabc.png)
 
Adicionalmente, realice las siguentes transformaciones durante el desarrollo de algunos de los requerimientos mencionados anteriormente y otras por mi cuenta, con el objetivo de implementar mejores practicas y solventar posibles inconvenientes en consultas posteriores:

  * Acostumbro a revisar y analizar los nulos durante el proceso de tratamiento de los datos, por tal motivo mientras realizaba el reemplazo de los valores  **`NaN`** por el string **`g`** en el campo rating, me di cuenta de algunos valores truncados en el archivo ***netflix_titles-score.csv*** y ***hulu_titles-score.csv***  hayados en los campos de **`rating`** y **`duration`**:
  
**En el caso del csv de Netflix**:
  
  ![cap1](https://user-images.githubusercontent.com/111402986/213606807-9a275fe5-c922-4022-8765-e4225001e684.png)
  ![cap11](https://user-images.githubusercontent.com/111402986/213606831-12e29689-d710-4c2e-8ee1-2f1f843d83fd.png)
  ![cap111](https://user-images.githubusercontent.com/111402986/213606845-9fce4f51-b988-410c-ac00-bc7874cb0288.png)
  
**En el caso del csv de Hulu**:
  
  ![cap2](https://user-images.githubusercontent.com/111402986/213607008-2f53bc49-4e24-4027-94f1-de6b31ad7779.png)
  ![cap22](https://user-images.githubusercontent.com/111402986/213607019-7d83f00e-584c-48cd-a63c-a60c8f62120f.png)
  ![cap222](https://user-images.githubusercontent.com/111402986/213607030-95cfdeab-1430-491e-b960-30bde0e994e2.png)
  ![cap2222](https://user-images.githubusercontent.com/111402986/213607038-f217b664-0a8a-4d17-9ef6-ce57c56f9b7d.png)
  ![cap22222](https://user-images.githubusercontent.com/111402986/213607041-8429c32f-e410-4327-8075-fce3d1312b8d.png)  

**En el caso del csv de Amazon y de Disney**

  Afortunadamente, para el csv de Amazon y Disney no encontramos valores truncados ni faltantes para la columna **`rating`**, por tal motivo durante el desarrollo de la transformación de reemplazar el string **`g`** por los **`NaN`** no representó inconvenientes particulares o significo transformaciones adicionales en el proceso.
  
**Finalmente...** Posterior a realizar todas las transformaciones requeridas por el analista de datos, procedí a unir todos los datasets en uno para posteriormente exportarlo como un dataset limpio, normalizado y listo para ser utilizado en el proceso del montaje y creación de la Api.
  
## **Desarrollo API**
  <i>(Para esta parte del proyecto además de implementar el mismo lenguaje de programación en conjunto con las librerias mencionadas anteriormente, también se implementó el uso del Framework ***`FastApi`*** y del modulo Uvicorn que nos permitió disponer de un servidor local para realizar las respectivas pruebas de la Api).</i>
  
  ![206626200-1577e4a8-be9c-4b91-8cce-d8ad19534399](https://user-images.githubusercontent.com/111402986/213611744-dffea9b6-860f-4c3e-a996-f096ad6401e8.png)
  
Importación y disponibilización del dataset desde GitHub debido a que en la parte de Deploy necesitabamos tenerno subido en la red:
  
  ![image](https://user-images.githubusercontent.com/111402986/213608976-acfb2eb5-a5f3-4480-860c-cc25371757d0.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213609123-0dacd8c5-bfff-4e3e-9543-bf7fbb7582e8.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213609251-a69d87bd-6200-443d-9ea6-7665079a17ef.png)

  ![image](https://user-images.githubusercontent.com/111402986/213609569-b31bd279-0e1f-421c-beb8-f6e0364c2b60.png)

  ![image](https://user-images.githubusercontent.com/111402986/213609647-44540d26-92df-47bc-b83b-3bedc6c8c9c8.png)
  
El objetivo del desarrollo de la APi consistia en disponibilizar los datos para que respondiera a las siguentes consultas:
  
* **Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma**
  
    ![image](https://user-images.githubusercontent.com/111402986/213609762-02190082-a3dc-485c-bc0c-c5ccaf7de089.png)
  
  La primera parte es repetitiva debido a que no estaba seguro si agregar una columna "plataforma" en el dataset original para hacer más eficiente el llamado o filtro por las plataformas. Adicionalmente, por medio de los condicionales, se hace la elección del dataframe filtrado a utilizar para asi, buscar la palabra en la columna titulos por medio del metodo **`contains`**
  
    ![image](https://user-images.githubusercontent.com/111402986/213610158-465fe66c-54e9-4f9b-88c4-75d05261e804.png)

    ![image](https://user-images.githubusercontent.com/111402986/213610240-f315d953-9451-44c2-9027-2cda1f1f2af3.png)

* **Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año**
  
  ![image](https://user-images.githubusercontent.com/111402986/213610432-af991578-40be-4bc7-8fc2-8e9884599096.png)
  
 El proceso logico es sencillo, el programa busca en el dataset de la plataforma pedida por el usuario, posterior a ello, realiza una conjunción entre la columna **`relase_year`** & **`score`**, finalmente aquellos que sean verdaderos, se guardan y al final se da el recuento de dicha cantidad de items.
  
  ![image](https://user-images.githubusercontent.com/111402986/213611438-86463736-27e3-4d08-b767-2054fad38647.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213611556-55f2dea5-0535-4d38-8da8-819f6586c317.png)

* La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos:
   
  ![image](https://user-images.githubusercontent.com/111402986/213612018-5f2fa432-dc33-4384-8d75-d9cd37fb7286.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213612061-de5d5e2b-4f03-4b29-9bf7-9ef8ee00df92.png)
 
 En el caso de esta función, organizamos los valores para los campos de **`score`** y **`title`** de manera descendente y el otro en orden alfabetico, el objetivo es que posteriormente al usar la función loc como mascara, podamos obtener un dataframe con las columnas de **`score`** y **`title`** solo que ahora ya solamente con los valores de las peliculas, por ultimo, el iloc nos permite obtener los 2dos valores de dicho dataframe y con el tolist()[0] o solamente llamando el primer elemento obtenemos el resultado
  
  ![image](https://user-images.githubusercontent.com/111402986/213612136-8e1925cd-1495-4447-a9bf-547492180884.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213612189-92e46606-6605-45fc-a582-c1941cdf3d69.png)

* **Película que más duró según año, plataforma y tipo de duración:**
  
  ![image](https://user-images.githubusercontent.com/111402986/213613367-f498f1d9-eb49-4a52-bc39-bf95d6e99585.png)
  
  Para esta query, solo debia de filtrarse por plataforma, realizar nuevamente una conjunción logica entre **`relase_year`** y **`duration_type`**, para al final encontrar el maximo valor en el campo **`duration_int`** el cual representara de acuerdo al proceso, la pelicula con mayor duración que cumpliera con todas las condiciones verdaderas.
  
 ![image](https://user-images.githubusercontent.com/111402986/213613491-33336ba2-f4e3-43fa-870b-da773311a526.png)
  
 ![image](https://user-images.githubusercontent.com/111402986/213613577-95572071-3d14-4daf-a60a-7ca88379126d.png)
 <i>(fijese que en este caso probamos la api pero en deta, obtenemos los mismos valores *mala mia por ese flotante que se coló xd).</i>

* **Cantidad de series y películas por rating:**
  En este caso, si trabajamos con todo el data.csv dado quenos piden un total general, al igual que la anteriores realizamos un filtrado al dataframe de la columna **`rating`** correspondiente a los valores que el cliente ponga en categoria y devolvemos el conteo de todos estos valores.
  
  ![image](https://user-images.githubusercontent.com/111402986/213614041-7af4b1ba-26e5-416a-ab40-919d358319e7.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213614104-61fcc436-3618-4006-90ac-e8b585674464.png)
  
  ![image](https://user-images.githubusercontent.com/111402986/213614282-9fd7702a-257b-4efb-abe9-51c2ee750097.png)
  
## **Deployment**
 <i>(El deployment fue realizado en ***`DETA`***, aparte de ello se dio disponibilidad abierta, la URL ya es publica y fue probada en diferentes lugares).</i>
  **https://oyn2rw.deta.dev/**  **https://oyn2rw.deta.dev/docs** <- **NO OLVIDAR PROBAR LA API Y SU DOCUMENTACION**
  
  ![Transmission-Shudders](https://user-images.githubusercontent.com/111402986/213615181-0f8e1f6f-acef-4511-9565-a5d2bfaa9461.jpg)

  Los comandos mas importantes en el desarrollo del proceso fueron: 
  * deta deploy, deta details, deta auth disable, deta visor enablee, deta --help 
  <i>(los comento porque realmente el desarrollo fue algo complicado dada la baja documentación y disponibilidad de la información para esta herramienta)</i>
  
  Posterior a usar el comando **`deta new --python (micro_newname)`**, obtendremos un json o diccionario con la informacón mas importante de nuestro micro creado, adicionalmnete, nos aparecera una carpeta **`.deta`** con los archivos que contienen toda la información de nuestro espacio, tambien tendremos un nuevo **`main.py`** que tendremos que modificar pegando el contenido del codigo que utilizamos anteriormente para la creación de la api y las queries, finalmente, no podremos olvidarnos de agregar el **`requeriments.txt`** con las dependencias que necesitemos, ya sea con diferente frameworks, librerias o modulos.
  ![image](https://user-images.githubusercontent.com/111402986/213616080-bab39584-4336-43d3-937e-c537fb099419.png)
  ![image](https://user-images.githubusercontent.com/111402986/213616750-3ef15d31-34e3-424a-895e-6be0ea7ba2b9.png)
  
  Por ultimo pero no menos importante, adjuntaré en esta parte algunas imagenes del producto final:
  
![image](https://user-images.githubusercontent.com/111402986/213615460-368744c1-e34f-4e5f-b461-8b4edf2a9e05.png)
![image](https://user-images.githubusercontent.com/111402986/213615548-8dbaa59f-e5be-4c2c-bfd4-9b8c12cb0825.png)
![image](https://user-images.githubusercontent.com/111402986/213615588-24c40915-1b66-4cf9-a115-7d5eda62b81d.png)
![image](https://user-images.githubusercontent.com/111402986/213615694-abb4c0b1-29b6-4c5e-8bfa-3b9b92443285.png)
![image](https://user-images.githubusercontent.com/111402986/213616022-67c65571-0093-464c-9cfa-3fecaf80cf89.png)
  
 ## **Video demostrativo**

El video demostrativo ejecutando las lineas mas importantes del codigo, incluyendo la presentacion general de todo el proyecto, el paso a paso y el producto final lo encontraran en el siguente enlace:
  
  

  
  
  
  
  
  
  
