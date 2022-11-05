import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from tqdm import tqdm
import inquirer
import bweb.bu as bweb
import sys

class Result:

    @staticmethod
    def generate(uf='', random = False, round = '2', model=0):
        data = bweb.BU.open_file(uf, round, model)
        if random:
            data = shuffle(data)
        sections_data = pd.DataFrame(columns=['percent', 'bozo', 'nine'])
        bozo = 0
        nine = 0
        count_section = 0
        count_percent = 0
        print('Contabilizando votos...')
        print('')
        for index, row in tqdm(data.iterrows(), total=len(data)):
            count_percent += 1
            percent = (count_percent / len(data)) * 100
            if row['NR_URNA_EFETIVADA'] not in sections_data.index:
                count_section += 1
            sections_data.loc[row['NR_URNA_EFETIVADA'],['percent']] = [percent]
            if row['NR_PARTIDO'] == 22:
                bozo += row['QT_VOTOS']
                bozo_percent = (bozo / (bozo + nine)) * 100
                if count_section > 1:
                    sections_data.loc[row['NR_URNA_EFETIVADA'],['bozo']] = [bozo_percent]
            if row['NR_PARTIDO'] == 13:
                nine += row['QT_VOTOS']
                nine_percent = (nine / (bozo + nine)) * 100
                if count_section > 1:
                    sections_data.loc[row['NR_URNA_EFETIVADA'],['nine']] = [nine_percent]

        print('')
        if model == 0:
            print('_________________RESULTADO (URNAS TODOS OS MODELOS)_____________________')
        if model == 1:
            print('_________________RESULTADO (URNAS MODELO 2020)_____________________')
        if model == 2:
            print('_________________RESULTADO (URNAS MODELO ANTERIOR A 2020)_____________________')
        print('')
        print('Total votos Bozo: ', bozo)
        print('Total votos Nine: ', nine)
        print('Total de seções: ', count_section)
        return sections_data



UFs = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'ZZ']
question = [inquirer.List('uf', message="Por favor, informe um estado (UF)",choices=UFs)]
input = inquirer.prompt(question)
print('')
print('Aguarde...')
print('')
chart_data_all = Result().generate(input['uf'])
chart_data_current = Result().generate(input['uf'], model=1)
chart_data_old = Result().generate(input['uf'], model=2)
#create charts
fig, axs = plt.subplots(3, constrained_layout=True)
fig.suptitle('Votação: ' + input['uf'])
chart_data_current.plot(x='percent', ax=axs[0], title='Urnas modelo 2020', grid=True)
chart_data_old.plot(x='percent', ax=axs[1], title='Urnas modelo anterior a 2020', grid=True)
chart_data_all.plot(x='percent', ax=axs[2], title='Todos os modelos', grid=True)
plt.show()
#sys.exit()
