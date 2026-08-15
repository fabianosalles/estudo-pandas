# 5. Analisar e criar gráficos

## Estatísticas do número de filhos

O projeto pede média, mediana, desvio padrão, moda, mínimo, máximo, contagem e quartis para `CL_FHL`.

```python
filhos = df["CL_FHL"]
print(filhos.mean())
print(filhos.median())
print(filhos.mode().iloc[0])
print(filhos.quantile([0.25, 0.50, 0.75]))
```

Nesta base, a moda e a mediana são 0. A média é aproximadamente 1,15. Isso mostra que muitos clientes não têm filhos, embora existam valores de 1 a 4.

## Agrupamento 1: compras por gênero

```python
compras = df.drop_duplicates(subset="CO_ID")
compras_por_genero = compras.groupby("CL_GENERO")["CO_ID"].nunique()
```

Primeiro guardamos apenas uma linha por compra. Depois contamos quantos identificadores únicos existem em cada gênero.

## Agrupamento 2: itens por categoria

```python
itens_por_categoria = df.groupby("PR_CAT").size()
```

`size()` conta linhas de cada grupo. Neste caso, ele mede itens/linhas de produtos, não faturamento, pois a base não possui coluna de preço.

## Gráfico com matplotlib

O projeto usa somente `matplotlib` para gráficos. Ele funciona em notebook e também no script `.py`.

```python
compras_por_genero.plot(kind="bar")
plt.title("Compras únicas por gênero")
plt.tight_layout()
plt.savefig("resultados/compras_por_genero.png")
```

`savefig()` salva a imagem, então o gráfico aparece como arquivo mesmo quando o código é executado no terminal.

## Como escrever uma conclusão

Fale somente sobre o que os dados permitem concluir. Exemplo: “ALIMENTOS teve mais itens registrados”. Não diga “ALIMENTOS faturou mais”, porque não existe preço ou valor da compra na base.
