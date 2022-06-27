@ECHO off
:: executar script dentro da pasta auth_upload_files
:: criação de ambiente
py -3 -m venv venv
:: instalação de bibliotecas
venv\Scripts\pip install -r requirements.txt
:: criação de banco de dados
venv\Scripts\python create_db.py
:: criação do diretorio de para armazenar as imagens
mkdir  project\static\uploads
