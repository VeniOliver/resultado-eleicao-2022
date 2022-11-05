import pandas as pd
import sys

headers = [
'DT_GERACAO',
'HH_GERACAO',
'ANO_ELEICAO',
'CD_TIPO_ELEICAO',
'NM_TIPO_ELEICAO',
'CD_PLEITO',
'DT_PLEITO',
'NR_TURNO',
'CD_ELEICAO',
'DS_ELEICAO',
'SG_UF',
'CD_MUNICIPIO',
'NM_MUNICIPIO',
'NR_ZONA',
'NR_SECAO',
'NR_LOCAL_VOTACAO',
'CD_CARGO_PERGUNTA',
'DS_CARGO_PERGUNTA',
'NR_PARTIDO',
'SG_PARTIDO',
'NM_PARTIDO',
'DT_BU_RECEBIDO',
'QT_APTOS',
'QT_COMPARECIMENTO',
'QT_ABSTENCOES',
'CD_TIPO_URNA',
'DS_TIPO_URNA',
'CD_TIPO_VOTAVEL',
'DS_TIPO_VOTAVEL',
'NR_VOTAVEL',
'NM_VOTAVEL',
'QT_VOTOS',
'NR_URNA_EFETIVADA',
'CD_CARGA_1_URNA_EFETIVADA',
'CD_CARGA_2_URNA_EFETIVADA',
'CD_FLASHCARD_URNA_EFETIVADA',
'DT_CARGA_URNA_EFETIVADA',
'DS_CARGO_PERGUNTA_SECAO',
'DS_AGREGADAS',
'DT_ABERTURA',
'DT_ENCERRAMENTO',
'QT_ELEITORES_BIOMETRIA_NH',
'DT_EMISSAO_BU',
'NR_JUNTA_APURADORA',
'NR_TURMA_APURADORA'
]

class BU:

    #open csv file
    @staticmethod
    def open_file(uf, round = '2', model=0):
        #model 0 (ALL)
        #model 1 (2020) = NR_URNA >= 2000000
        #model 2 (2009 - 2015) = NR_URNA <= 1950000
        #open csv file
        file = './bweb/csv/bweb_' + str(round) + 't_' + str(uf) + '_311020221535.csv'
        reader = pd.read_csv(file, encoding='latin1', sep = ';')
        #create data frame
        data = pd.DataFrame(reader, columns=headers)
        #filter president role
        data = data.loc[(data['CD_CARGO_PERGUNTA'] == 1) & ((data['NR_PARTIDO'] == 22) | (data['NR_PARTIDO'] == 13))]
        #data = data.loc[(data['CD_CARGO_PERGUNTA'] == 1)]
        #filter model
        if model == 1:
            data = data.loc[data['NR_URNA_EFETIVADA'] >= 2000000]
        if model == 2:
            data = data.loc[data['NR_URNA_EFETIVADA'] <= 1950000]
        #return filtered data
        return data
