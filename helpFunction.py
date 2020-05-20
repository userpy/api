from netaddr import IPAddress, IPNetwork
import json

from werkzeug.exceptions import HTTPException

class NetworkCalk:
    def __init__(self, hostaddres, mask):
        self.mask_len = IPAddress(mask).netmask_bits()
        self.ip = IPNetwork(f'{hostaddres}/{self.mask_len}')
        self.hostaddres = hostaddres
        self.networkPrefix = f"{self.ip.network}/{self.mask_len}"


class JsonCRUDErros(HTTPException):
    code = 500
    description = 'CRUD ERROR: file does not exist'

class JsonCRUDErrosAccept(HTTPException):
    code = 406
    description = 'CRUD ERROR: NOT ACCEPTABLE, IP alreadey exist'

class JsonCRUDErrosDelete(HTTPException):
    code = 406
    description = 'CRUD ERROR: DELETE , IP does not exist'

class JsonCRUD:
    def __init__(self, network, ip):
        self.network = network
        self.ip = ip
        self.filename = f'{self.network}.json'.replace('/', '-')
        self.rusult = None


    def write_addres_in_json(self):
        try:
            with open(self.filename, 'r') as f:
                json_in_file = f.read()
                try:
                    poolIpAddress = json.loads(json_in_file)
                    if self.ip in list(map(lambda x:x['ip'], poolIpAddress)):
                        raise JsonCRUDErrosAccept

                except json.decoder.JSONDecodeError:
                    poolIpAddress = []

            with open(self.filename, 'w') as f:
                poolIpAddress.append({'network': self.network, 'ip': self.ip})
                json.dump(poolIpAddress, f)
                self.rusult = 'ip address added to existing file'



        except FileNotFoundError:
            with open(self.filename, 'w') as f:
                json.dump([{'network': self.network, 'ip': self.ip}], f)
                self.rusult = 'ip address added to new file'


    def delete_addres_in_json(self):
        try:
            with open(self.filename, 'r') as f:
                json_in_file = f.read()
                poolIpAddress = json.loads(json_in_file)
                if self.ip in list(map(lambda x: x["ip"], poolIpAddress)):
                    pulipaddres = list(filter(lambda x: x["ip"] != self.ip, poolIpAddress))
                else:
                    raise JsonCRUDErrosDelete

            with open(self.filename, 'w') as f:
                json.dump(poolIpAddress, f)
                self.rusult = 'ip deleted'


        except FileNotFoundError:
            raise JsonCRUDErros
