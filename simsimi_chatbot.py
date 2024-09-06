import requests
import simsimi_chatbot

def get_simsimi_response(user_input):
    url = "https://api.simsimi.com/request.p?key=tOjnbnxpdPk7W_dNgdZSZNgQWUxyrLDVVH1M5t3l&lc=ko&ft=1.0&text=version" + user_input
    response = requests.get(url)
    data = response.json()
    return data['response']
def main():
    while True:
        user_input = input("You SimSimi: SimSimi, now this")
        if user_input.lower() == 'exit':
            print("Terminate the chatbot.")
            break
        response = simsimi_chatbot.get_simsimi_response(user_input)
        print("SimSimi: Yourself, sure ask" + response)
 with open('fixed_syntax.py', 'r', encoding='utf-8') as file:
       content = file.read()

   # Replace non-break spaces with regular spaces
   content = content.replace('\u00a0', ' ')

   with open('fixed_syntax.py', 'w', encoding='utf-8') as file:
       file.write(content)

if __name__ == '__main__':
    main()
