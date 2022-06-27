# Projeto de envio de arquivos com autenticação utilizando biblioteca **FLASK** do **Python**

Compatível com Windows, Linux, Mac

## Requisitos
Python 3.10 ou superior

É recomendado a criação de ambiente virtual para execução do projeto:

**ATENÇÃO Execute o comando dentro do diretorio do projeto!**

No linux:
<a id="ancora1"></a>
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

**ATENÇÃO [Ative](#ancora1) o seu ambiente antes executar esses comandos!**

*Será criado o ambiente python e criado a base de dados*


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


Acesse página do [signup](http://127.0.0.1:8085/signup), para criar o usuário com *username* **admin**

## Execução do projeto

Para executar o projeto siga os passos:

**ATENÇÃO [Ative](#ancora1) o seu ambiente antes executar esses comandos!**

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
