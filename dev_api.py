from flask import Flask, jsonify, request, json

app = Flask(__name__)

desenvolvedores = [
    {
     'id':0,
      'nome':'Marcos',
     'habilidades':['python', 'flask']
     },
    {
    'id':1,
     'nome': 'Carla',
     'habilidades': ['Java', 'jsf']
     }
]

#altera, delega e busca um dev pelo id
@app.route("/dev/<int:id>", methods=['GET','PUT','DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'message':'dev nao existe'}
        except Exception:
            response = {'status':'erro', 'message':'erro desconhecido'}

    elif request.method == 'PUT':
        #recupera o json enviado no body
        dados = json.loads(request.data)
        #seta o json no
        desenvolvedores[id] = dados
        response = desenvolvedores[id]
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        response = {'SUCESSO':'REgistro excluido'}

    return jsonify(response)

#lista todos os deves e inclui um novo dev
@app.route("/dev/", methods=['POST', 'GET'])
def lista_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        response = {'Status':'sucesso: posicao: {}'.format(posicao), 'message':'registro inserido'}

    elif request.method == 'GET':
        response = desenvolvedores

    return jsonify(response);






if __name__ == '__main__':
    app.run(debug=True)