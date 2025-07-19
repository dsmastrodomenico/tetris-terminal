# Usa una imagen base de Python ligera
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos y el código fuente del juego
COPY requirements.txt .
COPY tetris/ ./tetris/

# Instala las dependencias de Python (si las hubiera)
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar el juego cuando se inicie el contenedor
CMD ["python", "-m", "tetris.main"]