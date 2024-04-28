import re

def get_valid_filters(filters: dict) -> dict:
    filtros = {}

    campos_filtros = {
        'data_atendimento': ('data_atendimento', str, r'\d{4}-\d{2}-\d{2}$'),
        'condicao_saude': ('condicao_saude', str, 'hipertensao|diabetes|ferida vascular|dengue|tuberculose'),
        'unidade': ('unidade', str, None)
    }

    for parametro, (campo, tipo, valor_permitido) in campos_filtros.items():
        valor = filters.get(parametro)
        if valor:
            if tipo is not None and not isinstance(valor, tipo):
                raise TypeError(f'O parâmetro "{parametro}" deve ser do tipo {tipo.__name__}.')

            if valor_permitido is not None and not re.match(valor_permitido, valor):
                raise ValueError(f'O valor do parâmetro "{parametro}" deve estar no formato correto.')

            if parametro == 'data_atendimento':
                filtros[campo] = {'$regex': f'^{valor}.*'}
            else:
                filtros[campo] = valor

    if filtros == {}:
        ValueError(f"Nenhum filtro passado é valido, use somente os filtros: {','.join(campos_filtros.keys())}")

    return filtros