from dotenv import load_dotenv
from src.visualization.visualize import receita_por_pagamento, servicos_populares, receita_por_profissional
from src.data.driveBot import driveBot
from src.data.transform_dataframe import transform_data
import os
import requests
import json

load_dotenv()

class TelegramBot():
    def __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"
        self.drive_bot_instance = driveBot()

    def start(self):
        update_id = None
        while True:
            update = self.get_message(update_id)
            messages = update['result']
            if messages:
                for message in messages:
                    try:
                        update_id = message['update_id']
                        chat_id = message['message']['from']['id']
                        message_text = message['message']['text']
                        answer_bot, figure_boolean = self.create_answer(message_text)
                        self.send_answer(chat_id, answer_bot, figure_boolean)
                    except Exception as e:
                        print(f"Error processing message: {e}")


    def get_message(self, update_id):
        link_request = f"{self.url}getUpdates?timeout=1000"
        if update_id:
            link_request = f"{self.url}getUpdates?timeout=100&offset={update_id + 1}"
        result = requests.get(link_request)
        return json.loads(result.content)

    def create_answer(self, message_text):
        dataframe = transform_data(self.drive_bot_instance.get_data())
        if message_text in ["/start","oi", "ola", "eae","menu", "oie"]:
            return (
                "Olá, tudo bem? Seja bem vindo ao Bot do Salão do Stella Cabeleireiros. Selecione o que deseja:\n"
                "1 - Receita por pagamento\n"
                "2 - Serviços populares\n"
                "3 - Receita por profissional\n",
                0
            )
        elif message_text == "1":
            return receita_por_pagamento(dataframe), 1
        elif message_text == "2":
            return servicos_populares(dataframe), 1
        elif message_text == "3":
            return receita_por_profissional(dataframe), 1
        else:
            return (
                "Não entendi... por favor tente novamente...\n"
                "Selecione o que deseja:\n"
                "1 - Receita por pagamento\n"
                "2 - Serviços populares\n"
                "3 - Receita por profissional\n",
                0
            )
    def send_answer(self, chat_id, answer, figure_boolean):
        if figure_boolean == 0:
            link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={answer}"
            requests.get(link_to_send)
            return
        else:
            answer.seek(0)
            requests.post(f"{self.url}sendPhoto?chat_id={chat_id}", files = dict(photo=answer))
            answer.close()
            return