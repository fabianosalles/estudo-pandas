"""Análise exploratória simples da base varejo.csv.

Execute com: python analise_varejo.py
"""

import os
from pathlib import Path

# "Agg" permite salvar gráficos sem abrir uma janela, inclusive no terminal.
os.environ["MPLCONFIGDIR"] = str(Path(".matplotlib"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


# 1. CONFIGURAÇÃO E LEITURA
ARQUIVO_DADOS = "varejo.csv"
PASTA_RESULTADOS = Path("resultados")
PASTA_RESULTADOS.mkdir(exist_ok=True)

# O arquivo usa ponto e vírgula como separador.
df = pd.read_csv(ARQUIVO_DADOS, sep=";")

print("=" * 60)
print("1. CONHECENDO A BASE ORIGINAL")
print("=" * 60)
print(f"Registros: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")
print("\nTipos de dados:")
print(df.dtypes)
print("\nPrimeiras linhas:")
print(df.head())


# 2. QUALIDADE DOS DADOS
print("\n" + "=" * 60)
print("2. VERIFICANDO A QUALIDADE DOS DADOS")
print("=" * 60)
print("\nValores nulos por coluna:")
print(df.isna().sum())
print(f"\nLinhas totalmente duplicadas: {df.duplicated().sum()}")

# As quatro últimas colunas estão vazias em todas as linhas do arquivo.
colunas_vazias = df.columns[df.isna().all()].tolist()
print(f"\nColunas totalmente vazias: {colunas_vazias}")

# Contamos datas que não seguem o formato dia/mês/ano.
datas_teste = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
print(f"Datas inválidas: {datas_teste.isna().sum()}")
print("\nCategorias encontradas:")
print(df["PR_CAT"].value_counts(dropna=False))


# 3. LIMPEZA DOS DADOS
print("\n" + "=" * 60)
print("3. LIMPANDO A BASE")
print("=" * 60)

# Removemos somente colunas que não possuem nenhum valor.
df = df.dropna(axis=1, how="all")

# A base não possui nulos em PR_CAT, mas possui o valor #N/D.
# Em vez de apagar esses registros, usamos um rótulo claro.
df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")
df["PR_CAT"] = df["PR_CAT"].str.strip().replace("#N/D", "Sem Categoria")

# Removemos apenas linhas idênticas em todas as colunas.
# Não removemos CO_ID repetido: uma compra pode ter vários produtos.
linhas_antes = len(df)
df = df.drop_duplicates().copy()
print(f"Duplicatas removidas: {linhas_antes - len(df)}")

# Convertendo texto para data. Datas inválidas se transformariam em NaT.
df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
print(f"Datas inválidas após a conversão: {df['DATA'].isna().sum()}")
print(f"\nRegistros após a limpeza: {df.shape[0]}")
print("Tipos após a limpeza:")
print(df.dtypes)

# Salvamos uma cópia para uso posterior ou para entregar com o projeto.
arquivo_limpo = PASTA_RESULTADOS / "varejo_limpo.csv"
df.to_csv(arquivo_limpo, index=False, encoding="utf-8-sig")
print(f"\nArquivo limpo salvo em: {arquivo_limpo}")


# 4. ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS
print("\n" + "=" * 60)
print("4. ESTATÍSTICAS DA COLUNA CL_FHL (NÚMERO DE FILHOS)")
print("=" * 60)
filhos = df["CL_FHL"]
estatisticas_filhos = pd.Series(
    {
        "contagem": filhos.count(),
        "média": filhos.mean(),
        "mediana": filhos.median(),
        "desvio padrão": filhos.std(),
        "moda": filhos.mode().iloc[0],
        "mínimo": filhos.min(),
        "1º quartil": filhos.quantile(0.25),
        "2º quartil": filhos.quantile(0.50),
        "3º quartil": filhos.quantile(0.75),
        "máximo": filhos.max(),
    }
)
print(estatisticas_filhos.round(2))


# 5. AGRUPAMENTOS
print("\n" + "=" * 60)
print("5. AGRUPAMENTOS")
print("=" * 60)

# Uma compra pode ter diversos produtos. Para contar compras, usamos cada CO_ID uma vez.
compras = df.drop_duplicates(subset="CO_ID").copy()
compras_por_genero = (
    compras.groupby("CL_GENERO")["CO_ID"].nunique().sort_values(ascending=False)
)
print("\nCompras únicas por gênero:")
print(compras_por_genero)

itens_por_categoria = df.groupby("PR_CAT").size().sort_values(ascending=False)
print("\nItens vendidos por categoria:")
print(itens_por_categoria)

compras_por_mes = compras.groupby(compras["DATA"].dt.to_period("M"))["CO_ID"].nunique()
print("\nCompras únicas por mês:")
print(compras_por_mes)


# 6. GRÁFICOS (somente matplotlib)
plt.figure(figsize=(8, 4))
compras_por_genero.plot(kind="bar", color=["#4C78A8", "#F58518"])
plt.title("Compras únicas por gênero")
plt.xlabel("Gênero")
plt.ylabel("Quantidade de compras")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(PASTA_RESULTADOS / "compras_por_genero.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 4))
itens_por_categoria.plot(kind="bar", color="#54A24B")
plt.title("Quantidade de itens por categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de itens")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(PASTA_RESULTADOS / "itens_por_categoria.png", dpi=150)
plt.close()
print("\nGráficos salvos na pasta resultados.")


# 7. CONCLUSÕES
print("\n" + "=" * 60)
print("6. CONCLUSÕES")
print("=" * 60)
print(f"- Foram removidas {linhas_antes - len(df)} linhas totalmente duplicadas.")
print(f"- A categoria com mais itens é: {itens_por_categoria.index[0]}.")
print(f"- O gênero com mais compras únicas é: {compras_por_genero.index[0]}.")
print(f"- A moda do número de filhos é: {filhos.mode().iloc[0]}.")
print("- CO_ID repetido não é erro: ele identifica produtos da mesma compra.")
print("- Não há nulos nesta versão, mas #N/D foi tratado como Sem Categoria.")
