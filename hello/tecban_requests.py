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

        return response.json()