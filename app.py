from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('amazon.html', part='part1')

@app.route('/elenco')
def elenco():
    df = pd.read_csv('data/dati.csv')  
    return render_template('amazon.html', tabella=df.to_html(), part='part2', prodotti=df['immagini'].tolist(),nome=df['nome'].tolist(),prezzo=df['prezzo'].tolist(),quantità=df['quantità'].tolist(),categoria=df['categoria'].tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
