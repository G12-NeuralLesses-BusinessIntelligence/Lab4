# Lab4
Laboratorio 4 - Bussiness Intelligence 

# Instrucciones de despliegue de la API en un ambiente local

## Dependencias y librerías

Para la ejecución es importante instalar las siguientes librerías. Se recomienda hacerlo en un virtual environment de Python para evitar conflictos con distintas versiones o demás librerías:

<ul>
  <li>anyio==3.6.2</li>
<li>click==8.1.3</li>
<li>colorama==0.4.6</li>
<li>fastapi==0.85.2</li>
<li>h11==0.14.0</li>
<li>httptools==0.5.0</li>
<li>idna==3.4</li>
<li>joblib==1.2.0</li>
<li>numpy==1.23.4</li>
<li>pandas==1.5.1</li>
<li>pydantic==1.10.2</li>
<li>python-dateutil==2.8.2</li>
<li>python-dotenv==0.21.0</li>
<li>pytz==2022.6</li>
<li>PyYAML==6.0</li>
<li>scikit-learn==1.1.3</li>
<li>scipy==1.9.3</li>
<li>six==1.16.0</li>
<li>sniffio==1.3.0</li>
<li>starlette==0.20.4</li>
<li>threadpoolctl==3.1.0</li>
<li>typing_extensions==4.4.0</li>
<li>uvicorn==0.19.0</li>
<li>watchfiles==0.18.0</li>
<li>websockets==10.4</li>
</ul>

No obstante, debería ser suficiente con ejecutar los siguientes comandos en un virtual environment para que las librerías necesarias queden instaladas:

```
pip install fastapi
pip install "uvicorn[standard]" 
pip install pandas
pip install -U scikit-learn
```
## Ejecución del servidor

Para ejecutar el servidor, usaremos el siguiente comando en la consola de comandos.

```
uvicorn main:app --reload
```

## Importante revisar previamente

Debido a que en ejecuciones anteriores se pudo haber usado el segundo endpoint generando un modelo nuevo reentrenado, si queremos usar el modelo generado durante el laboratorio 3 debemos entrar a la carpeta \assets, eliminar el archivo <i>modelo.joblib</i>, duplicar el archivo  <i>modelo_base.joblib</i> y cambiar su nombre a <i>modelo.joblib</i>.

## Uso del primer endpoint

En Postman elegiremos una request POST y en la URL colocaremos la siguiente:

http://127.0.0.1:8000/predict

El contenido de la petición será de tipo <i>Body</i> y <i>RAW</i> enviando un archivo JSON. En el campo de texto copiamos y pegamos el JSON del escenario al cuál le queremos realizar la predicción.

<img width="885" alt="image" src="https://user-images.githubusercontent.com/54145170/199639397-ffb8fe1c-d3a2-4f4b-9103-ca44606dda90.png">

Finalmente, presionamos el botón <b>Send</b> y la respuesta de la ejecución nos saldrá en la sección de abajo.

<img width="900" alt="image" src="https://user-images.githubusercontent.com/54145170/199639437-5490c6d8-a805-4856-873a-0e80db178b9d.png">

## Uso del segundo endpoint

En Postman elegiremos una request POST y en la URL colocaremos la siguiente:

http://127.0.0.1:8000/retraining

El contenido de la petición será de tipo <i>Params</i> y en la tabla <i>Query Params</i> colocaremos lo siguiente:

<ul>
  <li>KEY: "data_in"</li>
  <li>VALUE: Aquí irá el JSON del escenario que vamos a ejecutar.</li>
</ul>

Finalmente, presionamos el botón <b>Send</b> y la respuesta de la ejecución nos saldrá en la sección de abajo.

<img width="895" alt="image" src="https://user-images.githubusercontent.com/54145170/199639655-ba45833d-fcf6-40a6-b0bd-5ba114151aee.png">

