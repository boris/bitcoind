import json
import requests
from requests.auth import HTTPBasicAuth

class BitcoinRPC():
    def __init__(self, rpc_user, rpc_password):
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.rpc_connection = "https://btc.borisquiroz.dev"
    
    def _call_rpc(self, method, params=None):
        headers = {'content-type': 'application/json'}
        payload = json.dumps({
            "jsonrpc": "1.0",
            "id": "python-bitcoinrpc",
            "method": method,
            "params": params or []
        })
        response = requests.post(
            self.rpc_connection,
            data=payload,
            headers=headers,
            auth=HTTPBasicAuth(self.rpc_user, self.rpc_password),
        )

        response.raise_for_status()
        return response.json()

    def getblockcount(self):
        response = self._call_rpc("getblockcount")
        msg = f"Current block count: {response['result']}"
        return msg

    def getchaintips(self):
        response = self._call_rpc("getchaintips")
        msg = f"Chain tips: {response['result']}"
        return msg


