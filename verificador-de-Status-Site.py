import requests, os
from dotenv import load_dotenv
load_dotenv()

def enviar_notificacao_telegram(mensagem):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("AVISO: Credenciais do Telegram não configuradas no arquivo .env. Notificação não enviada.")
        return
    url_api = f"https://api.telegram.org/bot{token}/sendMessage"
    # Parâmetros da requisição
    payload = {
        'chat_id': chat_id,
        'text': mensagem,
        'parse_mode': 'Markdown' # Permite usar negrito, itálico, etc.
    }
    
    try:
        # Envia a notificação
        response = requests.post(url_api, data=payload, timeout=10)
        if response.status_code != 200:
            print(f"ERRO: Falha ao enviar notificação para o Telegram. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"ERRO: Não foi possível conectar à API do Telegram. Erro: {e}")

class Requests:
    def __init__(self, lista_de_sites=[]):
        self.lista_de_sites = lista_de_sites
    def verificação(self):
        # Verifica se a lista não está vazia
        if not self.lista_de_sites:
            print("Você não digitou nenhum site.")
            return
        # Define um User-Agent para simular um navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Itera sobre a lista de sites
        for site in self.lista_de_sites:
            # Garante que o site tenha o protocolo (https://)
            # Se já tiver 'http', não faz nada. Se não, adiciona 'https://'.
            if not site.startswith(('http://', 'https://')):
                url_para_verificar = "https://" + site
            else:
                url_para_verificar = site
            
            # Tenta fazer a requisição para a URL formatada
            try:
                # Adicionado um timeout para não ficar esperando indefinidamente
                response = requests.get(url_para_verificar, timeout=10, headers=headers)
                # Verifica se o status code indica sucesso (2xx)
                if 200 <= response.status_code < 300:
                    print(f"✅ Site Online: {url_para_verificar} (Status: {response.status_code})")
                else:
                    mensagem = f"🚨 *ALERTA DE STATUS* 🚨\n\nO site `{url_para_verificar}` retornou um status inesperado.\n\n*Status Code:* {response.status_code}"
                    print(f"❌ Status Inesperado: {url_para_verificar} (Status: {response.status_code})")
                    enviar_notificacao_telegram(mensagem)
            
            # Se ocorrer qualquer erro de conexão (site não existe, sem internet, etc.)
            except requests.exceptions.RequestException as e:
                print(f"❌ Site Offline ou Erro: {url_para_verificar} não pôde ser alcançado.")
                mensagem = f"🔥 *SITE OFFLINE* 🔥\n\nNão foi possível conectar ao site `{url_para_verificar}`.\n\nO servidor pode estar inacessível."
                enviar_notificacao_telegram(mensagem)

if __name__ == "__main__":
    input_de_sites = input("Digite os sites e use espaços para separar: \n> ")
    # Filtra entradas vazias caso o usuário digite espaços extras
    lista_de_sites = [site for site in input_de_sites.split(" ") if site]
    script = Requests(lista_de_sites)
    script.verificação()