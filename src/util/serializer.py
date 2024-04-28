from bson import ObjectId


def serialize_resultado(resultado: ObjectId) -> ObjectId:
    resultado['_id'] = str(resultado['_id'])
    return resultado