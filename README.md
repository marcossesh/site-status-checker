# Monitor de Status de Sites com Notificações no Telegram

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Requests](https://img.shields.io/badge/Requests-Library-red?style=for-the-badge)

Um script simples em Python para monitorar o status de uma lista de sites. Caso um site esteja offline ou retorne um código de status inesperado (diferente de 2xx), uma notificação de alerta é enviada para um chat do Telegram.

---

## 🚀 Funcionalidades

- **Verificação de Status:** Envia requisições HTTP para uma lista de URLs para verificar se estão online.
- **Validação Inteligente:** Checa se o status code da resposta está na faixa de sucesso (200-299).
- **Notificações Imediatas:** Utiliza um bot do Telegram para enviar alertas em tempo real quando um site apresenta problemas.
- **Fácil de Usar:** Basta executar o script e inserir os sites que deseja monitorar, separados por espaços.
- **Configuração Segura:** Mantém suas credenciais (token do bot e chat ID) seguras usando variáveis de ambiente com um arquivo `.env`.

---

## 🛠️ Pré-requisitos

Antes de começar, você precisará ter o Python 3 instalado em sua máquina. Além disso, você precisa criar um bot no Telegram para obter as credenciais necessárias.

1.  **Crie um Bot no Telegram:**
    * Converse com o [BotFather](https://t.me/BotFather) no Telegram.
    * Use o comando `/newbot` para criar um novo bot.
    * Guarde o **token de acesso (API token)** que ele fornecer.
2.  **Obtenha o Chat ID:**
    * Envie uma mensagem para o seu novo bot.
    * Acesse a seguinte URL no seu navegador, substituindo `SEU_TOKEN_AQUI` pelo token que você guardou:
        ```
        [https://api.telegram.org/botSEU_TOKEN_AQUI/getUpdates](https://api.telegram.org/botSEU_TOKEN_AQUI/getUpdates)
        ```
    * Procure pelo campo `"chat":{"id": SEU_CHAT_ID}` na resposta. O valor `SEU_CHAT_ID` é o que você precisa.

---

## ⚙️ Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio
    ```

2.  **Instale as dependências:**
    É recomendado usar um ambiente virtual (virtualenv).
    ```bash
    # Crie um ambiente virtual (opcional)
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

    # Instale as bibliotecas necessárias
    pip install requests python-dotenv
    ```
    Ou, crie um arquivo `requirements.txt` com o seguinte conteúdo:
    ```txt
    requests
    python-dotenv
    ```
    E instale com:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais do Telegram:
    ```env
    # .env
    TELEGRAM_TOKEN="SEU_TOKEN_DO_BOT_AQUI"
    TELEGRAM_CHAT_ID="SEU_CHAT_ID_AQUI"
    ```
    **Importante:** Adicione o arquivo `.env` ao seu `.gitignore` para não expor suas credenciais no GitHub.

---

## ▶️ Como Usar

Execute o script a partir do seu terminal (neste exemplo, o arquivo se chama `monitor.py`):

```bash
python monitor.py
```
O script solicitará que você digite os sites que deseja monitorar. Insira as URLs separadas por um espaço e pressione Enter.
```
Exemplo de uso:

Digite os sites e use espaços para separar: 
> google.com github.com site-que-nao-existe.com.br
```
Saída esperada no terminal:
```
✅ Site Online: [https://google.com](https://google.com) (Status: 200)
✅ Site Online: [https://github.com](https://github.com) (Status: 200)
❌ Site Offline ou Erro: [https://site-que-nao-existe.com.br](https://site-que-nao-existe.com.br) não pôde ser alcançado.
```
---

## 💡Como o Código Funciona

enviar_notificacao_telegram(mensagem): Esta função é responsável por formatar e enviar a mensagem de alerta para a API do Telegram usando as credenciais do arquivo .env.

class Requests: A classe principal que contém a lógica para verificar os sites.

O método verificação() itera sobre a lista de sites fornecida.

Ele adiciona https:// automaticamente a URLs que não possuem um protocolo.

Utiliza um try...except para capturar erros de conexão (site offline, DNS não encontrado).

Verifica se o código de status da resposta está entre 200 e 299. Se não estiver, ou se ocorrer um erro de conexão, a função de notificação do Telegram é acionada.
