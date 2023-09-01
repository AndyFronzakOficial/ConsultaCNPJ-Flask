from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def consultar_cnpj(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except Exception as e:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        empresa = consultar_cnpj(cnpj)
        if empresa:
            return render_template('resultado.html', empresa=empresa)
        else:
            return 'Erro ao consultar o CNPJ. Verifique se o CNPJ é válido e tente novamente.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
