import socket



# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la IP y el puerto del servidor
server_ip = '0.0.0.0'  
server_port = 12349

# Vincular el socket a la dirección y puerto
server_socket.bind((server_ip, server_port))

# Escuchar conexiones entrantes (máximo 5 en espera)
server_socket.listen(5)
print(f"Servidor escuchando en {server_ip}:{server_port}")

# Aceptar la conexión del cliente
client_socket, client_address = server_socket.accept()
print(f"Conexión aceptada de {client_address}")

# Recibir datos del cliente
while True:
    data = client_socket.recv(1024)  # Recibe 1024 bytes a la vez
    if not data:
        break
    print(f"Cliente: {data.decode('utf-8')}")

    # Enviar respuesta al cliente
    message = input("Servidor: ")
    #agregar encriptacion
    client_socket.send(message.encode('utf-8'))

# Cerrar la conexión
client_socket.close()
server_socket.close()
