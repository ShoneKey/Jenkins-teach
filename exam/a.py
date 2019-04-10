class IOString():
    def get_string(self):
        self.s=input('请输入字符串:')

    def print_string(self):
        print(self.s.upper())




import requests
import json
resp=requests.get('http://www.weather.com.cn/data/sk/101190408.html')
city=resp.json()['weatherinfo']['city']
temp=resp.json()['weatherinfo']['temp']
print('{}:{}'.format(city.encode().decode(),temp.encode().decode('utf8')))

msg=json.loads(resp.content.decode())
print(msg['weatherinfo']['city'])
print(msg['weatherinfo']['temp'])