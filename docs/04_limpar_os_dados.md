# 4. Limpar os dados

Limpeza não é apagar dados sem pensar. Cada mudança deve ter uma justificativa.

## 1. Remover colunas totalmente vazias

```python
df = df.dropna(axis=1, how="all")
```

As colunas extras não contêm informação em nenhuma linha, então podem ser removidas.

## 2. Tratar categorias ausentes ou inválidas

```python
df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")
df["PR_CAT"] = df["PR_CAT"].str.strip().replace("#N/D", "Sem Categoria")
```

Em vez de excluir uma linha que tenha categoria ausente, mantemos a venda e usamos um rótulo que deixa o problema visível. `str.strip()` remove espaços antes e depois do texto.

## 3. Remover duplicatas completas

```python
df = df.drop_duplicates().copy()
```

`drop_duplicates()` sem parâmetros remove apenas linhas iguais em todas as colunas. O `.copy()` deixa claro que a nova tabela será usada nas próximas etapas.

## 4. Converter a data

```python
df["DATA"] = pd.to_datetime(
    df["DATA"], format="%d/%m/%Y", errors="coerce"
)
```

Antes, `DATA` era texto. Depois, é uma data (`datetime`), o que permite agrupar por mês. Se aparecesse uma data inválida, `errors="coerce"` a transformaria em `NaT`, facilitando sua identificação.

## Salvar a base limpa

```python
df.to_csv("resultados/varejo_limpo.csv", index=False, encoding="utf-8-sig")
```

`index=False` evita salvar a numeração das linhas como uma coluna extra.
