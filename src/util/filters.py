
def get_valid_filters(filters: dict) -> dict:
    filtros = {}

    campos_filtros = {
        'data_atendimento': 'data_atendimento',
        'condicao_saude': 'condicao_saude',
        'unidade': 'unidade'
    }

    for parametro, campo in campos_filtros.items():
        valor = filters.get(parametro)
        if valor:
            if parametro == 'data_atendimento':
                filtros[campo] = {'$regex': f'^{valor}.*'}
            else:
                filtros[campo] = valor