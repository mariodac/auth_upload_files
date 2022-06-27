# executar script dentro da pasta auth_upload_files, modificar o caminho abaixo de acordo com o diretorio que você salvou
cd /opt/auth_upload_files-main/
# criação de ambiente
python3 -m venv venv
# instalação de bibliotecas
venv/bin/pip install -r requirements.txt
# instalação do banco de dados
venv/bin/python3 create_db.py
# criação do diretorio de para armazenar as imagens
mkdir project/static/uploads
# concedendo permissão para script
chmod +x run.sh
