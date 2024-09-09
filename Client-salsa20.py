import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Función para cifrar los datos
def encrypt_salsa20(key, plaintext, nonce):
    cipher = Cipher(algorithms.Salsa20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    return ciphertext

# Función para descifrar los datos
def decrypt_salsa20(key, ciphertext, nonce):
    cipher = Cipher(algorithms.Salsa20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext)
    return plaintext

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 12345

# Conectar al servidor
client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

# Recibir la llave simétrica y el nonce del servidor
key_nonce = client_socket.recv(40)  # 32 bytes para la llave, 8 bytes para el nonce
key = key_nonce[:32]
nonce = key_nonce[32:]
print("Llave simétrica y nonce recibidos")

# Enviar y recibir mensajes cifrados
while True:
    message = input("Cliente (sin cifrar): ").encode('utf-8')

    # Cifrar el mensaje
    encrypted_message = encrypt_salsa20(key, message, nonce)
    client_socket.send(encrypted_message)

    # Recibir la respuesta cifrada del servidor
    data = client_socket.recv(1024)
    
    # Descifrar la respuesta
    decrypted_message = decrypt_salsa20(key, data, nonce)
    print(f"Servidor (descifrado): {decrypted_message.decode('utf-8')}")

    if message.decode('utf-8').lower() == "salir":
        break

# Cerrar la conexión
client_socket.close()