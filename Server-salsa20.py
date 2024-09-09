import socket
from Crypto.Cipher import Salsa20
import os

# Función para cifrar los datos
def encrypt_salsa20(key, plaintext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Función para descifrar los datos
def decrypt_salsa20(key, ciphertext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12349

server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Servidor escuchando en {server_ip}:{server_port}")

# Aceptar la conexión del cliente
client_socket, client_address = server_socket.accept()
print(f"Conexión aceptada de {client_address}")

# Generar una llave simétrica de 256 bits y un nonce de 8 bytes
key = os.urandom(32)  # Salsa20 requiere una llave de 32 bytes
nonce = os.urandom(8)  # Nonce de 8 bytes para Salsa20

# Enviar la llave y el nonce al cliente
client_socket.send(key + nonce)
print("Llave simétrica y nonce enviados al cliente")

# Recibir y enviar mensajes cifrados
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    
    # Descifrar el mensaje recibido
    decrypted_message = decrypt_salsa20(key, data, nonce)
    print(f"Cliente (descifrado): {decrypted_message.decode('utf-8')}")
    print(f"Cliente (encriptado): {data}")
    if decrypted_message.decode('utf-8') == "bye":
        break
    
    # Enviar respuesta cifrada al cliente
    message = input("Servidor (sin cifrar): ").encode('utf-8')
    encrypted_message = encrypt_salsa20(key, message, nonce)
    client_socket.send(encrypted_message)

# Cerrar la conexión
client_socket.close()
server_socket.close()