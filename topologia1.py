import os
import requests
from base64 import b64encode

def upload_file_to_github(repo, path, file_name, content, token):
    url = f"https://api.github.com/repos/{repo}/contents/{path}/{file_name}"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    data = {
        "message": f"Add {file_name}",
        "content": b64encode(content).decode("utf-8")
    }
    response = requests.put(url, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    repo = "AdsonVilla/topology1"
    path = "Users\adson\Cisco Packet Tracer 8.2.2\saves"
    file_name = "task1.pkt"
    token = os.getenv("GITHUB_TOKEN")

    with open("Users\adson\Cisco Packet Tracer 8.2.2\saves\task1.pkt", "rb") as file:
        content = file.read()
        response = upload_file_to_github(repo, path, file_name, content, token)
        print(response)

    file_name = "print-topologia.png"
    with open("Users\adson\OneDrive\Documentos\Adson Villacorta\print-topologia.png", "rb") as file:
        content = file.read()
        response = upload_file_to_github(repo, path, file_name, content, token)
        print(response)

    file_name = "ping.png"
    with open("caminho/para/seu/ping.png", "rb") as file:
        content = file.read()
        response = upload_file_to_github(repo, path, file_name, content, token)
        print(response)
