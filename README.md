# Mini-projeto: análise exploratória de dados de varejo

Este repositório apresenta uma Análise Exploratória de Dados (AED) da base `varejo.csv`. O objetivo é transformar dados brutos em informações: verificar a qualidade da base, limpar os dados, calcular estatísticas e responder perguntas simples sobre compras e produtos.

## Arquivos principais

- `analise_varejo.py`: solução completa para executar no VS Code ou terminal.
- `analise_varejo.ipynb`: a mesma solução, separada em células para usar no Jupyter ou Google Colab.
- `varejo.csv`: base de dados usada na análise.
- `docs/`: guias curtos para acompanhar a aula e entregar o projeto.

## Como executar

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python analise_varejo.py
```

O script cria a pasta `resultados/` com o arquivo `varejo_limpo.csv` e dois gráficos em PNG.

No Google Colab, envie `varejo.csv` e `analise_varejo.ipynb`; depois execute as células em ordem. Consulte [02 - Preparar o ambiente](docs/02_preparar_ambiente.md) para detalhes.

## Principais conclusões desta base

- A base original possui 830.000 registros; 96.553 deles são linhas totalmente duplicadas.
- Após remover os duplicados, restam 733.447 registros e 18.471 compras únicas.
- A categoria `ALIMENTOS` aparece em mais itens que as demais categorias.
- Há mais compras únicas de clientes do gênero `F` do que do gênero `M`.
- O número de filhos mais frequente é 0; a mediana também é 0 e a média é aproximadamente 1,15.
- Não há valores nulos nem datas inválidas nesta versão da base, mas existe a categoria `#N/D`, tratada como `Sem Categoria`.

## ETL e qualidade dos dados

ETL significa **Extrair, Transformar e Carregar**. Neste projeto, a extração é a leitura do CSV com pandas; a transformação inclui remover colunas vazias, padronizar a categoria, remover duplicatas e converter a data; o carregamento é salvar a versão limpa em CSV. A qualidade dos dados importa porque valores ausentes, tipos incorretos e duplicatas podem levar a conclusões erradas.

## Roteiro da aula

1. [Visão geral do desafio](docs/01_visao_geral.md)
2. [Preparar o ambiente](docs/02_preparar_ambiente.md)
3. [Conhecer a base](docs/03_conhecer_os_dados.md)
4. [Limpar os dados](docs/04_limpar_os_dados.md)
5. [Analisar e criar gráficos](docs/05_analise_e_graficos.md)
6. [Executar e entregar](docs/06_executar_e_entregar.md)
7. [Git e GitHub](docs/07_git_e_github.md)
