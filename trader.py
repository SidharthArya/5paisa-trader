from py5paisa import FivePaisaClient
import subprocess
import yaml
import os


class Trader:
    def __init__(self,creds, config):
        self.cred={
            "APP_NAME": creds["app_name"],
            "APP_SOURCE":creds["app_source"],
            "USER_ID":creds["user_id"],
            "PASSWORD": creds["password"],
            "USER_KEY":creds["user_key"],
            "ENCRYPTION_KEY":creds["encryption_key"]
        }
        self.config=config
        self.track_list = []
        self.refresh_config()
        self.client = FivePaisaClient(email=creds["user"], passwd=passw, dob=str(creds['dob']),cred=self.cred)

    def login(self):
        self.client.login()

    def market_status(self):
        return self.client.get_market_status()
    
    def get_quotes(self):
        return self.client.fetch_market_feed(self.track_list)
    def refresh_config(self):
        self.config=config
        self.track_list = []
        for k, v in self.config["track"].items():
            temp = {"Exch": k }
            for k1, v1 in v.items():
                temp["ExchType"] = k1
                for it in v1:
                    temp1 = temp.copy()
                    temp1["Symbol"] = it
                    self.track_list.append(temp1)
        

if __name__ == '__main__':
    p = subprocess.Popen(["pass", "Finance/5paisa.com"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode('utf-8')
    creds = yaml.safe_load(out.split("\n", 2)[2])
    with open(os.path.expanduser("~/Desktop/.stocks.yaml")) as f:
        tracks = yaml.safe_load(f)
    passw = out.split("\n", 1)[0]
    trader = Trader(creds, tracks)
    trader.login()
    print(trader.market_status())
    print(trader.get_quotes())
