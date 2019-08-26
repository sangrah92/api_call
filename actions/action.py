import requests as req

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, url):
        resp = req.get(url,timeout=6.0)
        print(resp.status_code)
	print(resp.url) 
