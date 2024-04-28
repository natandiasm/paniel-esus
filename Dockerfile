# Usa uma imagem base com Python
FROM python:3.11

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os requisitos da aplicação
COPY requirements.txt .

# Instala os requisitos
RUN pip install --no-cache-dir -r requirements.txt

# Copia o csv com os dados de atendimento
COPY atendimentos.csv .

# Copia a pasta da aplicação
COPY src src

# Faz o migrate do banco de dados e roda a aplicação
CMD python src/migrate.py && python src/app.py

# Libera a porta 8001 para a aplicação ser acessivel
EXPOSE 8001