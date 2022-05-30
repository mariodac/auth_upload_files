$env:FLASK_APP = "project"
$env:FLASK_DEBUG=1
$port=8085
$host_ip="127.0.0.1"
.\venv\Scripts\activate
flask run  --host=$host_ip --port=$port