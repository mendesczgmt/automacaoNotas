import datetime
import pandas as pd

shetname = '01 a 10.11'
caminhoNotas = 'C:\\Users\\Suporte\\downloads\\Emissões NF Sara Novembro Nova.xlsx'
lerPlanilha = pd.read_excel(caminhoNotas, sheet_name=shetname)

class Formatacao:
    def __init__(self):
        self._data = datetime.date.today().strftime('%d/%m/%Y')
        self._caminhoNotas = 'C:\\Users\\Suporte\\downloads\\Emissões NF Sara Novembro Nova.xlsx'
        self.shetname = '01 a 10.11'
        self._valor = 0
    
    def formatarValor(self, valor):
        self._valor = str(valor)
        self._valor += "00"
        self._valor = int(self._valor)
        return self._valor

    def get_data(self):
        return self._data

    def quantidadeNotas(self):
        tamanho = lerPlanilha.shape
        num_linhas = tamanho[0]
        return num_linhas
    
    def get_caminhoNotas(self):
        return caminhoNotas

    def get_pegarValor(self):
        self._valor = str(self._valor)
        self._valor += "00"
        self._valor = int(self._valor)
        return self._valor

    
