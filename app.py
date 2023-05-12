from flask import Flask, jsonify
import pandas as pd
from flask import render_template
from flask import request
from funcoes import *

app = Flask(__name__, template_folder='templates',
            static_folder='./templates/assets/')

# Aluno: Arthur Vinícius Santos Silva RA: 1903365

@app.route('/', methods=['GET', 'POST'])
def hello_word():
    if request.method == 'POST':
        var_name = request.form.get('fname')
        dict_ = {"0": {'frase': var_name}}
        teste = pd.DataFrame.from_dict(dict_, orient='index')
        teste.to_csv('teste.csv', sep=';', index=True)
        dados = pd.read_csv('./teste.csv', sep=';')
        frase = dados.frase.loc[0]
        string = traduz(frase)
        string = trata(string)
        dfim, pol, sub = previsao(string)
        if pol > 0.25:
            # fig = px.pie(dados, names='sentimento', values='polaridade')
            # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template('positive.html').format(pol)
        elif pol < -0.25:
            return render_template('negative.html').format(pol)
        else:
            return render_template('neutro.html').format(pol)

    return render_template('form.html')


app.run(debug=True)
