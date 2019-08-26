import sys
import requests 
import json

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, id):
        try:
            val=str(id)
            headers={'content-type': 'application/json'}
            url='https://fakerestapi.azurewebsites.net/api/Books/'+val
            response=requests.get(url,headers=headers,timeout=6.0)
            print(response)
            data2=response.json()
            print(data2)
        except requests.exceptions.Timeout:
            print("Request timeout")
            sys.exit(0)
