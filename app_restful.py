from flask import Flask, jsonify, request, json
from flask_restful import Resource, Api
from habilidades import Habilidade

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'message': 'dev nao existe'}
        except Exception:
            response = {'status': 'erro', 'message': 'erro desconhecido'}

        return response

    def put(self,id):
        # recupera o json enviado no body
        dados = json.loads(request.data)
        # seta o json no
        desenvolvedores[id] = dados
        response = desenvolvedores[id]

        return response

    def delete(self,id):
        desenvolvedores.pop(id)
        response = {'SUCESSO': 'REgistro excluido'}

        return response


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        response = {'Status': 'sucesso: posicao: {}'.format(posicao), 'message': 'registro inserido'}

        return response

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidade, '/habilidades/')



if __name__ == '__main__':
    app.run(debug=True)
