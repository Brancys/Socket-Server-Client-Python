import socket
from Crypto.Cipher import Salsa20

def encrypt_salsa20(key, plaintext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_salsa20(key, ciphertext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '172.17.4.213' # IP del servidor
server_port = 12349       # Puerto del servidor

# Conectarse al servidor
client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

# Recibir la clave simétrica y el nonce del servidor
key_nonce = client_socket.recv(1024)
key = key_nonce[:32]  # Salsa20 requiere una clave de 32 bytes
nonce = key_nonce[32:]  # Nonce de 8 bytes

print("Llave simétrica y nonce recibidos")

while True:
    message = input("Cliente (sin cifrar): ").encode('utf-8')
    encrypted_message = encrypt_salsa20(key, message, nonce) # Cifrar el mensaje
    client_socket.send(encrypted_message)

    data = client_socket.recv(1024)
    if not data:
        break

    decrypted_message = decrypt_salsa20(key, data, nonce) # Descifrar el mensaje
    print(f"Servidor (descifrado): {decrypted_message.decode('utf-8')}")
    print(f"Servidor (encrypt): {data}")

# Cerrar la conexión
client_socket.close()