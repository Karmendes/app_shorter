FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y libpq-dev gcc

# Folder on container
WORKDIR /app
# Copy the files for folder
COPY ./ .
# Install packages
RUN pip install --no-cache-dir -r requirements.txt
# Exposing
EXPOSE 5000
# Defina o comando para iniciar a aplicação Flask
CMD ["python", "app.py"]