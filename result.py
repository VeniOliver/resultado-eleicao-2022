import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from tqdm import tqdm
import inquirer
import bweb.bu as bweb
import sys

class Result:

    @staticmethod
    def generate(uf='', random = False, round = '2'):
        data = bweb.BU.open_file(uf, round)
        if random:
            data = shuffle(data)
        sections_data = pd.DataFrame(columns=['percent', 'bozo', 'nine'])
        bozo = 0
        nine = 0
        count_section = 0
        print('Contabilizando votos... /n')
        print('')
        for index, row in tqdm(data.iterrows(), total=data.shape[0]):
            if row['NR_URNA_EFETIVADA'] not in sections_data.index:
                count_section += 1
            percent = (count_section / len(data)) * 100
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

        print('_________________RESULTADO_____________________')
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
chart_data = Result().generate(input['uf'])
chart_data.plot(x='percent')
plt.show()
#sys.exit()
