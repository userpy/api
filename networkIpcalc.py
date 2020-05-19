from netaddr import IPAddress, IPNetwork




class NetworkCalk:
    def __init__(self, hostaddres, mask):
        self.mask_len = IPAddress(mask).netmask_bits()
        self.ip = IPNetwork(f'{hostaddres}/{self.mask_len}')
        self.hostaddres = hostaddres
        self.networkPrefix = f"{self.ip.network}/{self.mask_len}"


