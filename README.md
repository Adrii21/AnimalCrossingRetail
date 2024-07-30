# Animal Crossing Housewares E-commerce

Este proyecto es un e-commerce ficticio que muestra productos del juego Animal Crossing: New Horizons. La información sobre los productos se obtiene mediante un scraper, que recoge datos de una API y los almacena en una base de datos MongoDB. La aplicación web está construida utilizando Django para el backend y React para el frontend.

## Tecnologías Utilizadas

- **Backend**: Django
- **Frontend**: React
- **Base de Datos**: MongoDB
- **Mensajería Asíncrona**: Apache Kafka
- **Contenedores**: Docker
- **Entorno Virtual**: `virtualenv`

## Estructura del Proyecto

## Instalación

### Backend

1. **Crea un entorno virtual y activa:**

   ```bash
   cd backend
   virtualenv env
   source env/bin/activate
   Instala las dependencias:

bash

pip install -r requirements.txt

Configura el archivo settings.py:

Asegúrate de que la configuración de DATABASES esté apuntando a MongoDB:

python

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'products',
    }
}

Realiza las migraciones:

bash

python manage.py makemigrations
python manage.py migrate

Inicia el servidor de desarrollo:

bash

    python manage.py runserver

Frontend

    Navega al directorio frontend:

    bash

cd frontend

Instala las dependencias:

bash

npm install

Inicia el servidor de desarrollo:

bash

    npm start

Scripts

    Scraper

    El script scraper.py obtiene los datos de los productos y los publica en Kafka.

    bash

python scraper.py

Consumidor de Kafka

El script kafka_consumer.py consume los mensajes de Kafka y los almacena en MongoDB.

bash

    python kafka_consumer.py

Docker
Construir y Ejecutar Contenedores

    Para construir y ejecutar todos los contenedores:

    Desde la raíz del proyecto:

    bash

docker-compose up --build

Para detener los contenedores:

bash

    docker-compose down

Uso

    Backend: Accede a la API en http://127.0.0.1:8000/api/products/
    Frontend: Accede a la aplicación web en http://localhost:3000/
