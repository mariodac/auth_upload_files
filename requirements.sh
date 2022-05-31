#executar script dentro da pasta
python3 -m venv /opt/auth_upload_files-main/venv
/opt/auth_upload_files-main/venv/bin/pip install -r requirements.txt
mkdir /opt/auth_upload_files-main/project/static/uploads
chmod +x /opt/auth_upload_files-main/run.sh
