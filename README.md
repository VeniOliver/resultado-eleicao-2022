
# Resultado Eleições 2022

Um algorítimo simples para contabilização e análise dos votos das eleições 2022.

Os dados dos Boletins de Urnas estão disponíveis em: https://dadosabertos.tse.jus.br/dataset/resultados-2022-boletim-de-urna/


## IMPORTANTE

Esse é um algorítimo de análise de dados abertos e públicos disponibilizados pelo próprio Tribunal Superior Eleitoral - TSE.

Não é nosso objetivo contestar os resultados oficiais das eleições, apenas identificar anomalias estatísticas com poucas chances de ocorrer :)

## Contribuindo

Contribuições são sempre bem-vindas!

Por favor, siga o `código de conduta` desse projeto.


## Funcionalidades

- Contabilização do resultado por estado (UF)
- Contabilização do resultado por modelo de urna
- Identificação de Seções com mais de 98% de votos para um único candidato
- Identificação de Seções com mais de 90% de eleitores com biometria que não foram habilitados por meio dela


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

## Screenshots

![App Screenshot](https://i.ibb.co/d6pN2ny/alagoas.png)

![App Screenshot](https://i.ibb.co/M9yv71D/Captura-de-tela-de-2022-11-05-19-59-31.png)
