from flask import jsonify


def inicial_index():
    return jsonify({'mensagem': 'Bem vindo a imersão de Python com Flask API'})
