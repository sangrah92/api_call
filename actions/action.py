import requests as req

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, url):
        try:
		resp = req.get(url,timeout=6.0)
		print(resp.status_code)
		print(resp.url)
	except req.exceptions.MissingSchema:
                print("invalid URL")
                sys.exit(0)
	except req.exceptions.Timeout:
                print("Request timeout")
                sys.exit(0)
