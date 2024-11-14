
# %%
from extract import fazer_requisicoes_bancos, fazer_requisicoes_sociedades, extrair_dados
import time
import requests

# URL para a qual você deseja fazer a requisição

# Headers da requisição
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.bcb.gov.br/estabilidadefinanceira/balancetesbalancospatrimoniais',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
}

# %%

# ur = "https://www.bcb.gov.br/api/servico/sitebcb/Documentos/byListGuid?tronco=estabilidadefinanceira&guidLista=a11917e4-c729-4259-bd4e-0266827b6acd&ordem=DataDocumento%20desc&pasta=/Sociedades"

# x = requests.get(url=ur, headers=headers)



# %%


# %%
meses = [ "07", "08"]
anos = ["2024"]

combinacoes = [f"{ano}{mes}" for ano in anos for mes in meses]
for combinacao in combinacoes:
    response = fazer_requisicoes_bancos(data=combinacao, headers=headers)
    response2 = fazer_requisicoes_sociedades(data=combinacao, headers=headers)
    extrair_dados(response)
    extrair_dados(response2)
    print(combinacao)
    time.sleep(3)
    


