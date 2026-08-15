# 7. Git e GitHub

## O que são

- **Git** registra versões do projeto no computador.
- **GitHub** hospeda o repositório Git na internet.
- **Commit** é um ponto salvo no histórico, com uma mensagem curta sobre a mudança.

## Criar o repositório local

No terminal, dentro da pasta do projeto:

```powershell
git init
git add .
git commit -m "inicia mini projeto de varejo"
```

Faça novos commits durante o desenvolvimento, por exemplo:

```powershell
git add analise_varejo.py
git commit -m "adiciona limpeza dos dados"

git add README.md docs
git commit -m "documenta analise e conclusoes"
```

Não deixe todos os arquivos para um único commit final. Os commits devem mostrar o progresso real do projeto.

## Criar e enviar ao GitHub

1. Crie um repositório público no GitHub com o nome solicitado pela turma.
2. Copie a URL HTTPS do repositório criado.
3. Execute, trocando a URL:

```powershell
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

Depois de novos commits, use `git push` para enviá-los.

## Por que existe .gitignore?

O arquivo `.gitignore` diz ao Git o que não deve ser enviado. Neste projeto ele ignora:

- `.venv/`: ambiente virtual; cada pessoa cria o seu.
- `__pycache__/` e `*.pyc`: arquivos temporários do Python.
- `.ipynb_checkpoints/`: salvamentos automáticos do Jupyter.
- `.vscode/`: preferências locais do VS Code.

Neste mini-projeto, a pasta `resultados/` **não** é ignorada: o arquivo `varejo_limpo.csv` e os gráficos podem ser incluídos na entrega, conforme a orientação da atividade.

Não use uma regra ampla como `*.csv` sem pensar: isso também ignoraria a base `varejo.csv`, que pode ser necessária para executar o projeto. Se a base não puder ser publicada por tamanho ou licença, explique no README onde obtê-la.
