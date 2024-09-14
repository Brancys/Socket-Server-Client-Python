from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Llave, iv y mensaje cifrado capturados con Wireshark
key = bytes.fromhex('9be1e2b28faa390cb313c54fcaefb662d9ea449c29afeda1bdb448fc8a853b03')
iv = bytes.fromhex('81a43e8f58d7e969f862f8360a95fbd6')
msj = bytes.fromhex('a5624b25ba731144192acd6616f735a2')

cipher = AES.new(key, AES.MODE_CBC, iv)
# Descifrar el mensaje recibido
decrypted_data = cipher.decrypt(msj)
decrypted_data = unpad(decrypted_data, AES.block_size)
print('Mensaje descifrado:', decrypted_data.decode())