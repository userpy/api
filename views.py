from flask import request
from flask_restful import Resource

from helpFunction import NetworkCalk, JsonCRUD

class Index(Resource):
    def get(self):
        return {'info': 'CRUD: POST DELETE ','EXAMPLE':{"ip":"196.168.1.5", "mask":"255.255.255.0"}}

    def post(self):
        args = request.get_json(force=True)
        result =NetworkCalk(hostaddres=args.get('ip', None), mask=args.get('mask', None))

        network = result.networkPrefix
        ip = result.hostaddres

        crud = JsonCRUD(network=network, ip=ip)
        crud.write_addres_in_json()
        result = crud.rusult

        return {'network': network,'ip':ip, 'result':result}

    def delete(self):
        args = request.get_json(force=True)
        result = NetworkCalk(hostaddres=args.get('ip', None), mask=args.get('mask', None))

        network = result.networkPrefix
        ip = result.hostaddres

        crud=JsonCRUD(network=network, ip=ip)
        crud.delete_addres_in_json()
        result = crud.rusult

        return {'network': network,'ip':ip,'result':result}


