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

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.1.14'  # IP del servidor
server_port = 12349        

# Conectarse al servidor
client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

# Recibir la clave simétrica del servidor
key = client_socket.recv(1024)

print("Llave simétrica recibida")
#print("key: ", key.hex())

while True:
    # Enviar mensaje cifrado al servidor
    message = input("Cliente (sin cifrar): ").encode('utf-8')
    
    # Generar un nuevo nonce justo antes de enviar el mensaje
    nonce = os.urandom(8)
    
    # Cifrar el mensaje
    encrypted_message = encrypt_salsa20(key, message, nonce)
    
    # Enviar el nonce junto con el mensaje cifrado
    client_socket.send(nonce + encrypted_message)

    # Recibir respuesta del servidor
    data = client_socket.recv(1024)
    if not data:
        break

    nonce = data[:8]  # Los primeros 8 bytes son el nonce
    ciphertext = data[8:]  # El resto es el mensaje cifrado

    decrypted_message = decrypt_salsa20(key, ciphertext, nonce)  # Descifrar el mensaje
    print(f"Servidor (descifrado): {decrypted_message.decode('utf-8')}")
    #print(f"Servidor (encriptado): {ciphertext.hex()}")

# Cerrar la conexión
client_socket.close()
