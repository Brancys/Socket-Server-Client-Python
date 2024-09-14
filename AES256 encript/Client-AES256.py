import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Crear el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.7', 12349)) # Cambiar localhost a ip del servidor

# Recibir la clave y el IV del servidor
key_iv = client_socket.recv(1024)
iv = key_iv[:AES.block_size]  # El IV tiene el tamaño del bloque de AES
key = key_iv[AES.block_size:]  # La clave ocupa el resto de los datos

# Comunicación cíclica con el servidor
while True:
    # Ingresar el mensaje que se va a enviar al servidor
    message = input("Cliente (sin cifrar): ").encode()

    # Crear un nuevo cifrador AES con la clave y un nuevo IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_message = cipher.encrypt(pad(message, AES.block_size))

    # Enviar el mensaje cifrado al servidor
    client_socket.send(encrypted_message)

    # Recibir el IV y el mensaje cifrado del servidor
    iv_encrypted_data = client_socket.recv(1024)
    if not iv_encrypted_data:
        break

    # Separar el IV y los datos cifrados
    iv = iv_encrypted_data[:AES.block_size]
    encrypted_data = iv_encrypted_data[AES.block_size:]

    # Crear un nuevo cifrador AES con la nueva clave y IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Descifrar el mensaje
    decrypted_message = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    print('Servidor (descifrado):', decrypted_message.decode())

# Cerrar la conexión
client_socket.close()
