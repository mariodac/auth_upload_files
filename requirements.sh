#executar script dentro da pasta
cd /opt/auth_upload_files-main/
python3 -m venv venv
venv/bin/pip install -r requirements.txt
mkdir project/static/uploads
chmod +x run.sh
