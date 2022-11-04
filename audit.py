import sys
import pandas as pd
import bweb.bu as bweb
import inquirer

class Audit:
    unanimity_percent = 98
    unanimity_min = 20
    biometry_percent = 90
    biometry_min = 0
    unanimity_data = pd.DataFrame(columns=['NR_SECAO', 'NR_ZONA', 'NM_MUNICIPIO', 'SG_UF', 'PERCENT', 'QT_VOTOS', 'QT_COMPARECIMENTO', 'NM_PARTIDO'])
    biometry_data = pd.DataFrame(columns=['NR_SECAO', 'NR_ZONA', 'NM_MUNICIPIO', 'SG_UF', 'PERCENT', 'QT_VOTOS', 'QT_COMPARECIMENTO', 'QT_ELEITORES_BIOMETRIA_NH'])

    def get_percent(value, total):
        return (value / total) * 100

    def biometry(row):
        percent = Audit.get_percent(row['QT_ELEITORES_BIOMETRIA_NH'], row['QT_COMPARECIMENTO'])
        if row['QT_COMPARECIMENTO'] > Audit.biometry_min and percent >= Audit.biometry_percent:
            if row['NR_URNA_EFETIVADA'] not in Audit.biometry_data.index:
                Audit.biometry_data.loc[row['NR_URNA_EFETIVADA']] = [row['NR_SECAO'], row['NR_ZONA'], row['NM_MUNICIPIO'], row['SG_UF'], round(percent, 2), row['QT_VOTOS'], row['QT_COMPARECIMENTO'], row['QT_ELEITORES_BIOMETRIA_NH']]
                print('')
                print('Na seção %s na Zona %s em %s-%s %s (por cento, %s/%s) dos eleitores com biometria não foram habilitados por meio dela' % (row['NR_SECAO'], row['NR_ZONA'], row['NM_MUNICIPIO'], row['SG_UF'], round(percent, 2), row['QT_ELEITORES_BIOMETRIA_NH'], row['QT_COMPARECIMENTO']))

    def unanimity(index, row):
        percent = Audit.get_percent(row['QT_VOTOS'], row['QT_COMPARECIMENTO'])
        if row['QT_COMPARECIMENTO'] > Audit.unanimity_min and percent >= Audit.unanimity_percent:
            Audit.unanimity_data.loc[index] = [row['NR_SECAO'], row['NR_ZONA'], row['NM_MUNICIPIO'], row['SG_UF'], round(percent, 2), row['QT_VOTOS'], row['QT_COMPARECIMENTO'], row['NM_PARTIDO']]
            print('')
            print('Seção %s na Zona %s em %s-%s possui %s (por cento, %s/%s) dos votos para o %s' % (row['NR_SECAO'], row['NR_ZONA'], row['NM_MUNICIPIO'], row['SG_UF'], round(percent, 2), row['QT_VOTOS'], row['QT_COMPARECIMENTO'], row['NM_PARTIDO']))

    @staticmethod
    def verify(uf, round = '2'):
        data = bweb.BU.open_file(uf, round)
        for index, row in data.iterrows():
            Audit.unanimity(index, row)
            Audit.biometry(row)


choices = ['TODOS', 'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'ZZ']
UFs = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'ZZ']
question = [inquirer.List('uf', message="Por favor, informe um estado (UF)",choices=choices)]
input = inquirer.prompt(question)
print('')
print('Aguarde...')
print('')
if input['uf'] == 'TODOS':
    for uf in UFs:
        Audit().verify(uf)
else:
    Audit().verify(input['uf'])
