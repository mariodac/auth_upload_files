export FLASK_APP=project
export FLASK_DEBUG=1
port=8085
host_ip="127.0.0.1"
. venv/bin/activate
flask run --port="$port" --host="$host_ip"