from flask import Flask, jsonify, make_response, request

#Importa o banco de dados
from bd import Carros

#Instancia o modulo Flask na nossa variavel app
app = Flask('carros')

#Primeiro método - Visualizar Dados (GET)
# app.route -> definir que essa função é uma rota para que o flask entenda que aquele método precisa ser executado 
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros



#Primeiro método parte 2 - Visualizar Dados por ID (GET)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carro(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)


#Segundo método - Criar novos dados (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso', 
                carro=carro
                )
    )
    
#Terceiro método - Editar Dados (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])
        

#Quarto método - deletar (delete)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem:": "Carro excluido com sucesso!"})


app.run(port=5000, host='localhost')