from flask_restful import  Resource

habilidades = ['java', 'php', 'python']

class Habilidade(Resource):
    def get(self):
        return habilidades