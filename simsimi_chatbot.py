import requests

def get_simsimi_response(user_input):
    url = "https://api.simsimi.com/request.p?key=your_api_key&lc=ko&ft=1.0&text=" + user_input
    response = requests.get(url)
    data = response.json()
    return data['response']
