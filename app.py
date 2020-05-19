from flask import Flask
from views import Index
from flask_restful import  Api


app = Flask(__name__)
api = Api(app)
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run()
