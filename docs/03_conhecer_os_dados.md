# 3. Conhecer os dados antes de alterar

Comece sempre olhando a base original. No código, estas linhas fazem isso:

```python
df = pd.read_csv("varejo.csv", sep=";")
print(df.shape)
print(df.dtypes)
print(df.head())
```

`sep=";"` informa que as colunas do arquivo são separadas por ponto e vírgula. `shape` retorna `(linhas, colunas)`, `dtypes` mostra os tipos e `head()` exibe as primeiras linhas.

## Colunas importantes

- `DATA`: data da compra.
- `CO_ID`: identificador da compra.
- `CL_ID`: identificador do cliente.
- `CL_GENERO`: gênero do cliente.
- `CL_FHL`: número de filhos do cliente.
- `PR_CAT`: categoria do produto.
- `PR_NOME`: nome do produto.

## Verificações de qualidade

```python
print(df.isna().sum())
print(df.duplicated().sum())
print(df["PR_CAT"].value_counts(dropna=False))
```

Nesta base, aparecem quatro colunas completamente vazias no fim do CSV, 96.553 linhas totalmente duplicadas e a categoria `#N/D`. Não há valores nulos ou datas inválidas nesta versão.

## Uma regra de negócio importante

`CO_ID` pode aparecer em várias linhas. Isso não é uma duplicata: uma compra pode conter vários produtos. Por isso, removemos apenas linhas idênticas em todas as colunas e usamos `drop_duplicates(subset="CO_ID")` somente quando queremos contar compras únicas.
