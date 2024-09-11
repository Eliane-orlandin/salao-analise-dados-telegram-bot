import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

def receita_por_pagamento(file):
    buf = io.BytesIO()

    if not pd.api.types.is_numeric_dtype(file['Valor (R$)']):
        print("Coluna 'Valor (R$)' não é numérica!")
        return None
    
    receita_por_pagamento = file.groupby('Forma de Pagamento')['Valor (R$)'].sum()
    
    plt.figure(figsize=(10, 6))
    receita_por_pagamento.plot(kind='bar', color='skyblue')
    plt.title('Receita Total por Forma de Pagamento')
    plt.xlabel('Forma de Pagamento')
    plt.ylabel('Receita (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)  # Retornar ao início do buffer para leitura
    return buf

def servicos_populares(file):
    buf = io.BytesIO()

    if 'Serviço' not in file.columns or file['Serviço'].empty:
        print("Coluna 'Serviço' não encontrada ou está vazia!")
        return None
    
    servicos_populares = file['Serviço'].value_counts()
    
    plt.figure(figsize=(12, 8))
    servicos_populares.plot(kind='bar', color='lightgreen')
    plt.title('Serviços Mais Populares')
    plt.xlabel('Serviço')
    plt.ylabel('Número de Solicitações')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)  # Retornar ao início do buffer para leitura
    return buf

def receita_por_profissional(file):
    buf = io.BytesIO()

    if not pd.api.types.is_numeric_dtype(file['Valor (R$)']):
        print("Coluna 'Valor (R$)' não é numérica!")
        return None
    
    receita_por_profissional = file.groupby('Profissional')['Valor (R$)'].sum()
    
    plt.figure(figsize=(12, 8))
    receita_por_profissional.plot(kind='bar', color='salmon')
    plt.title('Receita Total por Profissional')
    plt.xlabel('Profissional')
    plt.ylabel('Receita (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)  # Retornar ao início do buffer para leitura
    return buf
