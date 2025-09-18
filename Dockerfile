# Le digo a Docker que quiero usar Python 3.7.11 pero la versión ligera para que pese menos
FROM python:3.7.11-slim

# Creo una carpeta dentro del contenedor donde voy a poner todo mi proyecto
WORKDIR /python-api

# Copio el archivo donde tengo todas las librerías que necesita mi proyecto
COPY requirements.txt requirements.txt

# Instalo todas las librerías que puse en requirements.txt
RUN pip install -r requirements.txt

# Copio todo lo demás del proyecto al contenedor
COPY . .

# Cuando arranque el contenedor, levanto mi servidor de Flask para que funcione la app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
