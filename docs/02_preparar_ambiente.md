# 2. Preparar o ambiente

## Pré-requisito

Instale o Python 3.10 ou superior e abra a pasta do projeto no VS Code. No VS Code, abra o terminal pelo menu **Terminal > New Terminal**.

## Criar um ambiente virtual

O ambiente virtual separa as bibliotecas deste projeto das bibliotecas de outros projetos.

No PowerShell, dentro da pasta do projeto, execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, abra-o como usuário normal e execute uma única vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois, feche e abra o terminal e ative novamente o ambiente. Quando ativo, o terminal começa com `(.venv)`.

No Prompt de Comando (cmd), o comando de ativação é:

```bat
.venv\Scripts\activate.bat
```

Para sair do ambiente ao final, use `deactivate`.

## Instalar as bibliotecas

Com `(.venv)` aparecendo no terminal:

```powershell
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` lista somente duas bibliotecas: `pandas` para os dados e `matplotlib` para os gráficos. O código foi feito para funcionar tanto em notebook como em arquivo `.py`.

## Criar ou atualizar requirements.txt

Depois de instalar novas bibliotecas no ambiente virtual, gere a lista completa com:

```powershell
python -m pip freeze > requirements.txt
```

Exemplo para adicionar uma biblioteca:

```powershell
python -m pip install nome-da-biblioteca
python -m pip freeze > requirements.txt
```

Use esse comando apenas com o ambiente do projeto ativado. Assim o arquivo não registra pacotes de outros projetos.

## Usar no Google Colab

Envie o notebook e o CSV ao Colab. O Colab já inclui pandas e matplotlib na maior parte das vezes. Caso uma biblioteca falte, execute em uma célula:

```python
!pip install -r requirements.txt
```
