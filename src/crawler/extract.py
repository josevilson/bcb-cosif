# %%

import requests
import os
import zipfile

def extrair_dados(response):
    if response == False:
        return print('nao encontrado!')
    else:

        local_zip_file = 'data/temp/arquivo.zip'
        extract_to = 'data/raw'

        with open(local_zip_file, 'wb') as file:
                file.write(response.content)
                print(f"Arquivo {local_zip_file} baixado com sucesso.")
        
        if os.path.exists(local_zip_file):
            with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"Arquivo descompactado com sucesso em {extract_to}.")
            try:
                if os.path.exists(local_zip_file):
                    os.remove(local_zip_file)
                    print(f"Arquivo apagado com sucesso! {local_zip_file}.")
            except:
                print(f"Erro ao remover o arquivo {local_zip_file}.")
        else:
            print(f"O arquivo {local_zip_file} não existe.")

def fazer_requisicoes_bancos(data, headers):
    
    url1 = f'https://www.bcb.gov.br/content/estabilidadefinanceira/cosif/Bancos/{data}BANCOS.ZIP'
    url2 = f'https://www.bcb.gov.br/content/estabilidadefinanceira/cosif/Bancos/{data}BANCOS.csv.zip'
    # Fazendo a requisição na primeira URL
    resposta1 = requests.get(url1, headers=headers)
    print(f"{url1}:{resposta1.status_code}")
    if resposta1.status_code == 200:
        
        return resposta1

    # Fazendo a requisição na segunda URL
    resposta2 = requests.get(url2, headers=headers)
    print(f"{url2}:{resposta2.status_code}")
    if resposta2.status_code == 200:
        return resposta2
    
    else:
        print("Nenhuma das URLs retornou um código de status 200")
        return False
def fazer_requisicoes_sociedades(data, headers):
    
    url3 = f'https://www.bcb.gov.br/content/estabilidadefinanceira/cosif/Sociedades/{data}SOCIEDADES.ZIP'
    url4 = f'https://www.bcb.gov.br/content/estabilidadefinanceira/cosif/Sociedades/{data}SOCIEDADES.csv.zip'

    resposta3 = requests.get(url3, headers=headers)
    print(f"{url3}:{resposta3.status_code}")
    if resposta3.status_code == 200:
        
        return resposta3

    # Fazendo a requisição na segunda URL
    resposta4 = requests.get(url4, headers=headers)
    print(f"{url4}:{resposta4.status_code}")
    if resposta4.status_code == 200:
        return resposta4
    
    else:
        print("Nenhuma das URLs retornou um código de status 200")
        return False