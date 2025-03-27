# importar biblioteca
from flask import Flask, jsonify
# importe para documentacao
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# [flask routes] para listar rotas da api

# criar variavel para receber a classe Flask
app = Flask(__name__)

#   documentacao OpenAPI
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)

@app.route('/<tipo_tempo>/<quantidade_tempo>')
def validade(tipo_tempo, quantidade_tempo):
    """

    :param tipo_tempo: tipo de tempo (dias, semanas, meses e anos)
    :param quantidade_tempo: quantidade de tempo de validade desde a data de fabricacao
    :return: retorna a data de fabricacao e a data de validade em relacao a data de fabricacao

    ## Resposta (JSON):
    '''json
    {
        'fabricacao': 27-03-2025,
        'validade': 27-03-2026,
    }
    '''
    """
    try:
        prazo = int(quantidade_tempo)
        meses = datetime.today()+relativedelta(months=prazo)
        anos = datetime.today()+relativedelta(years=prazo)
        semanas = datetime.today()+relativedelta(weeks=prazo)
        dias = datetime.today()+relativedelta(days=prazo)

        if tipo_tempo == 'meses':
            validade = meses
        elif tipo_tempo == 'anos':
            validade = anos
        elif tipo_tempo == 'semanas':
            validade = semanas
        elif tipo_tempo == 'dias':
            validade = dias


        return jsonify({
            'fabricacao': datetime.today().strftime('%d/%m/%Y'),
            'validade': validade.strftime('%d/%m/%Y')
        })

    except ValueError:
        return jsonify({
            'erro': "Valor Inválido"
        })


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)


