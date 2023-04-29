import json
import pause
import requests

LATENCY_OFFSET = 0.0125

def post(nickname):
    param = {'nickname': nickname}
    req = requests.post('http://18.178.127.171/challenges', json=param)
    result = json.loads(req.text)
    
    put(result['id'], result['actives_at'])
    
def put(id, active):
    wait = active * 1e-3 - LATENCY_OFFSET
    headers = {'X-Challenge-Id': id}
    
    pause.until(wait)
    res = requests.put('http://18.178.127.171/challenges', headers=headers)
    result = json.loads(res.text)
    
    try: 
        print(result['result'])
    except KeyError:
        put(result['id'], result['actives_at'])
        
if __name__ == '__main__':
    post('realive')