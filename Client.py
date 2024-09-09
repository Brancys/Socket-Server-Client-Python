import socket

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la IP y el puerto del servidor al que se va a conectar
server_ip = '172.24.32.1'  # Cambiar por la IP del servidor
server_port = 12349

# Conectar al servidor
client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

# Enviar y recibir datos del servidor
while True:
    message = input("Cliente: ")
    client_socket.send(message.encode('utf-8'))

    # Recibir la respuesta del servidor
    data = client_socket.recv(1024)
    print(f"Servidor: {data.decode('utf-8')}")

    if message.lower() == "salir":
        break

# Cerrar la conexión
client_socket.close()
