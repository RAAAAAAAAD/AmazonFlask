from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Carica i dati da un file CSV
df = pd.read_csv('data/dati.csv')

@app.route('/')
def home():
    return render_template('amazon.html', part='part1')

@app.route('/elenco')
def elenco():  
    return render_template('amazon.html', part='part2', prodotti=df['immagini'].tolist())

# Endpoint per fornire i dati come JSON
@app.route('/data', methods=['GET'])
def get_data():
    # Converte i dati in un dizionario JSON
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
