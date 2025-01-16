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
        return f"Current block count: {response['result']}"

    def getchaintips(self):
        response = self._call_rpc("getchaintips")
        result = json.dumps(response['result'], indent=4)
        return f"Chain tips: {result}"

    def getpeerinfo(self):
        response = self._call_rpc("getpeerinfo")
        print("Connected peers:")
        print("ID\tAddress")
        for peer in response['result']:
            print(f"{peer['id']}\t{peer['addr']}")
        return f"Total peers: {len(response['result'])}"

