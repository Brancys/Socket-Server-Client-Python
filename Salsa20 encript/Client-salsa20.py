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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.1.14'  # IP del servidor
server_port = 12349        

client_socket.connect((server_ip, server_port))
print(f"Conectado al servidor en {server_ip}:{server_port}")

key = client_socket.recv(1024)

print("Llave simétrica recibida")
#print("key: ", key.hex())

while True:
    message = input("Cliente (sin cifrar): ").encode('utf-8')
    
    nonce = os.urandom(8)    
    encrypted_message = encrypt_salsa20(key, message, nonce)    
    client_socket.send(nonce + encrypted_message)

    data = client_socket.recv(1024)
    if not data:
        break

    nonce = data[:8]  # Los primeros 8 bytes son el nonce
    ciphertext = data[8:]  

    decrypted_message = decrypt_salsa20(key, ciphertext, nonce)
    print(f"Servidor (descifrado): {decrypted_message.decode('utf-8')}")
    #print(f"Servidor (encriptado): {ciphertext.hex()}")

client_socket.close()
