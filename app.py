from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Carregando os dados do arquivo mobs.json
with open('mobs.json', 'r') as file:
    mobs_data = json.load(file)

@app.route('/monsters', methods=['GET'])
def get_monsters():
    try:
        # Obtendo os níveis dos jogadores A e B a partir dos parâmetros da requisição
        player_a_level = int(request.args.get('player_a_level'))
        player_b_level = int(request.args.get('player_b_level'))

        # Calculando os limites para a pesquisa no mobs.json
        x = max(1, player_a_level - 9)
        y = player_b_level + 9

        # Filtrando a lista de monstros com base nos limites calculados
        filtered_mobs = [mob for mob in mobs_data['monsters'] if x <= mob['Level'] <= y]

        return jsonify({'monsters': filtered_mobs})

    except ValueError:
        return jsonify({'error': 'Os níveis dos jogadores devem ser números inteiros.'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)