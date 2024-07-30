# Animal Crossing Housewares E-commerce

Este proyecto es un e-commerce ficticio que muestra productos del juego Animal Crossing: New Horizons. La información sobre los productos se obtiene mediante un scraper, que recoge datos de una API y los almacena en una base de datos MongoDB. La aplicación web está construida utilizando Django para el backend y React para el frontend.

## Tecnologías Utilizadas

- **Backend**: Django
- **Frontend**: React
- **Base de Datos**: MongoDB
- **Mensajería Asíncrona**: Apache Kafka
- **Contenedores**: Docker
- **Entorno Virtual**: `virtualenv`

## Instalación

### Backend

1. **Crea un entorno virtual y activa**

   ```bash
   cd backend
   virtualenv env
   source env/bin/activate

2. **Instala las dependencias**
   `pip install -r requirements.txt`
   
3. **Configura el archivo settings.py**

Asegúrate de que la configuración de DATABASES esté apuntando a MongoDB:
  
    DATABASES = {
          'default': {
              'ENGINE': 'djongo',
              'NAME': 'products',
          }
      }

4. **Realiza las migraciones**

      python manage.py makemigrations
      python manage.py migrate

5. **Inicia el servidor de desarrollo**

       python manage.py runserver

### Frontend

1. **Navega al directorio frontend**

         cd frontend

3. **Instala las dependencias**

         npm install

4. **Inicia el servidor de desarrollo**

          npm start

### Scripts

1. **Scraper**

El script scraper.py obtiene los datos de los productos y los publica en Kafka.

       python scraper.py

2. **Consumidor de Kafka**
El script kafka_consumer.py consume los mensajes de Kafka y los almacena en MongoDB.

    python kafka_consumer.py

## Docker

 ### Construir y Ejecutar Contenedores
 Desde la raíz del proyecto:

   1. **Para construir y ejecutar todos los contenedores**

            docker-compose up --build

3. **Para detener los contenedores**

          docker-compose down

Uso

   - Backend: Accede a la API en http://127.0.0.1:8000/api/products/
   - Frontend: Accede a la aplicación web en http://localhost:3000/
