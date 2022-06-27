# cria variavel para execução do flask
$env:FLASK_APP = "project"
# ativa servidor de desenvolvimento
$env:FLASK_DEBUG=1
# configura a porta do servidor
$port=8085
#altere para 0.0.0.0 para acessar de qualquer dispositivo que esteja na sua rede
$host_ip="127.0.0.1" 
# ativa o ambiente
.\venv\Scripts\activate
# executa servidor flask
flask run  --host=$host_ip --port=$port
