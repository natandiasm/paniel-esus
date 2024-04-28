import re
from flask import Blueprint, request, jsonify
from db.database import mongo

from util.serializer import serialize_resultado, get_valid_filters

routers = Blueprint("routers_v1", __name__)


@routers.route("/atendimentos/", methods=['GET'])
def routers_v1_atendimentos():
    collection = mongo.db['atendimentos']

    filtros = get_valid_filters(request.args)

    resultados = collection.find(filtros)

    serialized_resultados = [serialize_resultado(resultado) for resultado in resultados]

    return jsonify(serialized_resultados), 200
