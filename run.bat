@ECHO off
:: cria variavel para execução do flask
set FLASK_APP=project
:: ativa servidor de desenvolvimento
set FLASK_DEBUG=1
:: configura a porta do servidor
set port=8085
:: configura o host do servidor altere para 0.0.0.0 para acessar de qualquer dispositivo na mesma rede
set host_ip="127.0.0.1"
:: ativa o ambiente e executa o servidor flask
.\venv\Scripts\activate && flask run --port=%port% --host=%host_ip%
