$env:FLASK_APP = "project"
$env:FLASK_DEBUG=1
$port=8085
#altere para 0.0.0.0 para acessar de qualquer dispositivo que esteja na sua rede
$host_ip="127.0.0.1" 
.\venv\Scripts\activate
flask run  --host=$host_ip --port=$port
