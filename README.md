# Sobre o script:

Desenvolvi esses scripts, pois tive muitos problemas com o uso de fila na AWS, nesse caso utilizando a solução SQS.

Como nos projetos que atuei de tempos em tempos precisávamos mover mensagens entre fila no SQS, fez sentido o desenvolvimento desses scripts, pois não existe essa função nativa no SQS.

O script lambda.py pode ser utilizado no serviço Aws lambda, para que de forma automática mova as mensagens de uma fila  para  outra.

Essa função pode ser triggada pelo próprio SQS, ou seja, toda vez que uma mensagem cair na fila do trigger essa função irá move-la automaticamente para a fila desejada.

# Requisitos:

Python3
Boto3
OS

# Observações:

Caso não queira criar uma função lambda, basta executar em seu próprio computar o script app.py, para isso basta preencher as informações em branco no script e instalar o boto3 em seu computador.

Comando: python3 app.py