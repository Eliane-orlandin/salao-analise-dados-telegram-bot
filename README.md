# Análise de Dados para o Salão Stella

## Descrição

Este projeto é um bot para o Telegram que analisa dados de um salão de cabeleireiro chamado **Stella Cabeleireiros**. O bot coleta e analisa informações sobre serviços prestados, clientes, profissionais e pagamentos. O objetivo é fornecer insights úteis para a gestão do salão, como receita por pagamento, serviços mais populares e desempenho dos profissionais.

## Funcionalidades

- **Análise de Dados:** Coleta e analisa dados como Data, Nome do Cliente, Serviço, Profissional, Valor (R$), Forma de Pagamento.
- **Relatórios:** Gera relatórios sobre receita por pagamento, serviços populares e receita por profissional.
- **Interatividade:** Envia imagens de gráficos de barra após opção escolhida.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **Telegram API:** Para integração com o bot do Telegram.
- **Google Sheets API:** Para coleta e análise de dados.
- **Heroku:** Hospedagem do bot e serviços associados.

## Requisitos

- Python 3.8 ou superior
- Conta no Telegram e token do bot
- Conta do Google e credenciais da API do Google Sheets
- Conta no Heroku (opcional para implantação)

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/Eliane-orlandin/salao-analise-dados-telegram-bot.git
   cd salao-analise-dados-telegram-bot
   ```

2. **Crie um Ambiente Virtual e Instale as Dependências:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Execute o Bot:**

   ```bash
   python main.py
   ```

## Uso

1. **Inicie uma conversa com o bot no Telegram:**

   Encontre o bot usando o nome de usuário `@AnaliseDadosSalao_bot` e inicie uma conversa.

2. **Interaja com o Bot:**

   Use os comandos disponíveis para obter relatórios e análises de dados.

## Contribuição

Se você quiser contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para sua modificação (`git checkout -b feature/MinhaNovaFuncionalidade`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça o push para sua branch (`git push origin feature/MinhaNovaFuncionalidade`).
5. Envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, entre em contato com [Eliane Orlandin](mailto:liorlandin33@gmil.com).

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

# Visualizações

Análise de Receita por Forma de Pagamento
Análise de Serviços Mais Populares
Receita Total por Profissional
