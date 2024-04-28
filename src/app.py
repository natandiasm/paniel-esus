import os
from flask import Flask

from db.database import mongo
from routers.v1.core import routers

# Instancia o Flask
app = Flask(__name__)

# Adiciona o rota da API
app.register_blueprint(routers, url_prefix='/api/v1')

# Configura o mongo uri
app.config["MONGO_URI"] = "mongodb://painel_esus-mongo:27017/esus"

# Inicia o mongo na instancia do flask
mongo.init_app(app)


@app.route('/')
def index():
    count = mongo.db.atendimentos.count_documents({})
    return {"version": 0.1, "count_documents": count}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
