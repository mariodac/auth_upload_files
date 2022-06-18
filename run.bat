set FLASK_APP=project
set FLASK_DEBUG=1
set port=8085
:: altere para 0.0.0.0 para acessar de qualquer dispositivo na mesma rede
set host_ip="127.0.0.1"
.\venv\Scripts\activate && flask run --port=%port% --host=%host_ip%
