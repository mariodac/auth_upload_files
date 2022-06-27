# Projeto de envio de arquivos com autenticação utilizando biblioteca **FLASK** do **Python**

Compatível com Windows, Linux, Mac

## Requisitos
Python 3.10 ou superior

É recomendado a criação de ambiente virtual para execução do projeto:

**ATENÇÃO Execute o comando dentro do diretorio do projeto!**

No linux:
- Para criação do ambiente:
```
python3 -m venv venv
```
- Para ativar o ambiente:
```
. venv/bin/activate
```
No windows:
- Para criação do ambiente:
```
py -3 -m venv venv
```
- Para ativar o ambiente:
```
venv\Scripts\activate
```
Todos as bibliotecas e suas versões estão no arquivo [requisitos](requirements.txt)

Para instalar as bibliotecas siga os passos:

**ATENÇÃO Ative o seu ambiente antes executar esses comandos!**


No Linux:
```
venv/bin/pip install -r requirements.txt
```
Ou execute o [Script Shell](requirements.sh)

No windows:
```
venv\Scripts\pip install -r requirements.txt
```
Ou execute o [Script Batch](requirements.bat)

## Configuração do banco de dados

Na pasta project já está criado uma banco de dados, caso queira criar outro banco de dados siga o passos:

No linux:
```
venv/bin/python3
from project import db, create_app, models
db.create_all(app=create_app())
exit()
```
No windows:
```
venv\Scripts\python
from project import db, create_app, models
db.create_all(app=create_app())
exit()
```

## Execução do projeto

Para executar o projeto siga os passos:

**ATENÇÃO Ative o seu ambiente antes executar esses comandos!**

No Linux:
```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run --port=8085 --host=127.0.0.1
```
Ou execute o [Script Shell](run.sh)

No Windows:
```
set FLASK_APP=project
set FLASK_DEBUG=1
flask run --port=8085 --host=127.0.0.1
```
Ou execute o [Script Batch](run.bat), [Script Powershell](run.ps1)
