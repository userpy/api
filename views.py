from flask import request
from flask_restful import Resource

from networkIpcalc import NetworkCalk

class Index(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        args = request.get_json(force=True)
        result =NetworkCalk(hostaddres=args.get('ip', None), mask=args.get('mask', None))
        network = result.networkPrefix
        ip = result.hostaddres
        return {'network': network,'ip':ip}



