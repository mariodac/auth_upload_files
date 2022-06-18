cd /opt/auth_upload_files-main/
export FLASK_APP=project
export FLASK_DEBUG=1
port=8085
#altere para 0.0.0.0 para acessar de qualquer dispositivo que esteja na sua rede
host_ip="127.0.0.1"
. /opt/auth_upload_files-main/venv/bin/activate
flask run --port="$port" --host="$host_ip"
