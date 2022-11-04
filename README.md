
# Resultado Eleições 2022

Um algorítimo simples para contabilização e análise dos votos das eleições 2022.

Os dados dos Boletins de Urnas estão disponíveies em: https://dadosabertos.tse.jus.br/dataset/resultados-2022-boletim-de-urna/


## IMPORTANTE

Esse é um algorítimo de análise de dados abertos e públicos disponibilizados pelo próprio Tribunal Superior Eleitoral - TSE.

Não é nosso objetivo contestar os resultados oficiais das eleições.

## Contribuindo

Contribuições são sempre bem-vindas!

Por favor, siga o `código de conduta` desse projeto.


## Funcionalidades

- Contabilização de resultado por estado (UF)
- Identificação de Seções com mais de 98% de votos para um único candidato
- Identificação de Seções com mais de 90% de eleitores com biometria não foram habilitados por meio dela


## Instalação

Baixe resultado-eleicao-2022 com git

```bash
  git clone https://github.com/VeniOliver/resultado-eleicao-2022.git
  cd resultado-eleicao-2022
```
Baixe para o diretório `./bweb/csv/` os arquivos de Boletim de Urna disponíveis em:


```bash
  https://dadosabertos.tse.jus.br/dataset/resultados-2022-boletim-de-urna/
```
Execute os algorítimos

```bash
  python3 result.py
  python3 audit.py
```
