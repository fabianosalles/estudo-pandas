# 1. Visão geral do mini-projeto

## Objetivo

Fazer uma Análise Exploratória de Dados (AED) da base `varejo.csv`. AED é o primeiro contato organizado com os dados: observar como são, encontrar problemas, corrigir o que for necessário e tirar conclusões simples.

## O que será produzido

- Um script, `analise_varejo.py`, que funciona no VS Code ou no terminal.
- Um notebook, `analise_varejo.ipynb`, para executar por células no Jupyter ou Google Colab.
- Um arquivo limpo e dois gráficos, criados na pasta `resultados/` ao executar o script.

## Etapas da análise

1. Ler o CSV com pandas.
2. Verificar quantidade de linhas, colunas, tipos, nulos, duplicatas e datas.
3. Limpar os problemas encontrados.
4. Calcular estatísticas do número de filhos (`CL_FHL`).
5. Agrupar compras por gênero, categoria e mês.
6. Criar gráficos e escrever conclusões.

## Vocabulário básico

- **Registro/linha**: uma observação da tabela.
- **Coluna**: uma característica, como data ou categoria.
- **Duplicata**: linha repetida.
- **Nulo**: valor ausente, mostrado como `NaN` no pandas.
- **DataFrame**: tabela manipulada pelo pandas.

Siga os próximos arquivos na ordem. Execute um bloco de cada vez e leia o comentário antes de avançar.
