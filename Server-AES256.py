import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print('Esperando conexión del cliente...')
client_socket, address = server_socket.accept()
print('Cliente conectado:', address)

# Generar una clave AES de 256 bits y un IV
key = get_random_bytes(32)  # 32 bytes para AES-256
iv = get_random_bytes(AES.block_size)

# Enviar la clave y el IV al cliente
client_socket.send(iv + key)

# Comunicación cíclica con el cliente
while True:
    # Recibir datos cifrados del cliente
    encrypted_data = client_socket.recv(1024)
    if not encrypted_data:
        break

    # Crear el cifrador AES con el mismo IV y clave
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Descifrar el mensaje recibido
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_data, AES.block_size)
    print('Cliente (descifrado):', decrypted_data.decode())

    # Ingresar la respuesta del servidor
    message = input("Servidor (sin cifrar): ").encode()

    # Crear un nuevo cifrador AES con la misma clave y un nuevo IV
    iv = get_random_bytes(AES.block_size)  # Generar un nuevo IV para cada mensaje
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Cifrar el mensaje del servidor
    encrypted_message = cipher.encrypt(pad(message, AES.block_size))

    # Enviar el IV y el mensaje cifrado al cliente
    client_socket.send(iv + encrypted_message)

# Cerrar la conexión
client_socket.close()
server_socket.close()
