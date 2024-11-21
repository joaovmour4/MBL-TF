# Use uma imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Defina a variável de ambiente para Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Exponha a porta que o Flask usa (ajuste conforme necessário)
EXPOSE 8000

# Comando para executar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
