# %%
import pandas as pd
import glob
import chardet

class BcbCosif:
    def __init__(self) -> None:
        self.dtypes_config = {
                                '#DATA_BASE': str, 
                                'DATA_BASE': str, 
                                'DOCUMENTO': str, 
                                'CNPJ': str, 
                                'AGENCIA': str, 
                                'NOME_INSTITUICAO': str,
                                'COD_CONGL': str, 
                                'NOME_CONGL': str, 
                                'TAXONOMIA': str, 
                                'CONTA': str, 
                                'NOME_CONTA': str, 
                                'SALDO': 'float64'
                            }


    def ler_arquivo(self, arquivo_name: str) -> pd.DataFrame:
        try:
            df = pd.read_csv(arquivo_name, decimal=",", dtype=self.dtypes_config, encoding=self.encoding_file, skiprows=3, sep=";")
            df.columns = df.columns.str.strip()
            self.df = df

        except UnicodeDecodeError:
            # Tentativa de leitura com 'iso-8859-1'
            df = pd.read_csv(arquivo_name, decimal=",", dtype=self.dtypes_config, encoding='utf-8',  skiprows=3, sep=";")
            df.columns = df.columns.strip()
            self.df = df
    
    def save_df(self, path_to_save: str) -> None:
        self.df.to_csv(path_to_save, index=False, sep=';', decimal=',', encoding='utf-8')
        
    def _get_encoding(self, arquivo_name: str):
        with open(arquivo_name, 'rb') as arquivo:
            arquivo_byte = arquivo.read()

            resultado = chardet.detect(arquivo_byte)
            resultado = resultado['encoding'].lower()
            print(f'chardet detectado: {resultado}!')
            self.encoding_file = resultado

    def _replace_cabecalho(self, arquivo_name: str):
        with open(arquivo_name, 'r+', encoding=self.encoding_file) as arquivo:
            conteudo = arquivo.read()

            cabecalho_novo_correto = 'DATA_BASE;CNPJ;NOME_INSTITUICAO;ATRIBUTO;DOCUMENTO;CONTA;NOME_CONTA;SALDO'
            cabecalho_old = 'DATA;CNPJ;NOME INSTITUICAO;ATRIBUTO;DOCUMENTO;CONTA;NOME CONTA;SALDO                                                                                                  '

            if cabecalho_old in conteudo:
                novo_conteudo = conteudo.replace(cabecalho_old, cabecalho_novo_correto, 1)
                arquivo.seek(0)
                arquivo.write(novo_conteudo)

            if '#DATA_BASE;' in conteudo:
                novo_conteudo = conteudo.replace('#DATA_BASE;', 'DATA_BASE;', 1)
                arquivo.seek(0)
                arquivo.write(novo_conteudo)

# %%
if __name__ == "__main__":
    lista = glob.glob('../data/*1995*')
    for arquivo in lista:
        print(f'filename: {arquivo}')
        f = BcbCosif()
        f._get_encoding(arquivo)
        f._replace_cabecalho(arquivo)
        f.ler_arquivo(arquivo_name=arquivo)
        f.save_df(f'../output/{arquivo.split('/')[-1]}')
# %%
