import requests
import os
from django.conf import settings

class TecbanRequests():
    def __init__(self):
        TRANSPORT_CERT_KEY = os.path.join(settings.BASE_DIR, "client_private_key.key")
        TRANSPORT_CERT = os.path.join(settings.BASE_DIR, "client_certificate.crt")
        self.client = (TRANSPORT_CERT, TRANSPORT_CERT_KEY)

    def consentiment_accounts(self):
        headers = {
            "x-fapi-financial-id":"c3c937c4-ab71-427f-9b59-4099b7c680ab",
            "x-fapi-interaction-id": "15bbc01f-f883-4e91-88c6-b26245b9a35b",
            "Authorization": "Bearer 722f2c96-9bf3-4dbc-b521-fca81b60a67a"
        }
        
        response = requests.get(
            "https://rs1.tecban-sandbox.o3bank.co.uk/open-banking/v3.1/aisp/accounts",
            headers=headers,
            verify=False,
            cert=self.client)

        json = response.json()

        transactions = []
        for transaction in json["Data"]["Account"]:
            transactions.append(
                {
                    "type": transaction["AccountType"],
                    "name": transaction["Account"][0]["Name"],
                }
            )
        return transactions
    
    def balance_accounts(self):
        headers = {
            "x-fapi-financial-id":"c3c937c4-ab71-427f-9b59-4099b7c680ab",
            "x-fapi-interaction-id": "26b7b58f-b3e8-4dfb-8689-60f2e2edd4c6",
            "Authorization": "Bearer 722f2c96-9bf3-4dbc-b521-fca81b60a67a"
        }
        response = requests.get(
            "https://rs1.tecban-sandbox.o3bank.co.uk/open-banking/v3.1/aisp/balances",
            headers=headers,
            verify=False,
            cert=self.client)
        
        json = response.json()

        transactions = []
        for transaction in json["Data"]["Balance"]:
            transactions.append(
                {
                    "amount": transaction["Amount"]["Amount"]
                }
            )
        return transactions
    
    def account_extract(self):
        headers = {
            "x-fapi-financial-id":"c3c937c4-ab71-427f-9b59-4099b7c680ab",
            "x-fapi-interaction-id": "5558869e-fd1d-42f5-a6f7-5fa93719ece8",
            "Authorization": "Bearer 722f2c96-9bf3-4dbc-b521-fca81b60a67a"
        }
        
        response = requests.get(
            "https://rs1.tecban-sandbox.o3bank.co.uk/open-banking/" + 
            "v3.1/aisp/accounts/5f1864ac7af45c38b664522a/statements/"+ 
            "4d33a016-5747-4173-a99f-b084f8e3d300/transactions",
            headers=headers,
            verify=False,
            cert=self.client)

        json = response.json()

        transactions = []
        for transaction in json["Data"]["Transaction"]:
            transactions.append(
                {
                    "name": transaction["TransactionInformation"],
                    "amount": transaction["Amount"]["Amount"],
                    "date": transaction["ValueDateTime"]
                }
            )
        return transactions