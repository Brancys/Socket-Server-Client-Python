from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Cifrado
key = get_random_bytes(32)  # AES-256 usa una clave de 256 bits (32 bytes)
iv = get_random_bytes(16)   # IV de 128 bits (16 bytes)
mensaje = b"Este es un mensaje secreto"

# Crear el objeto de cifrado AES en modo CBC
cipher = AES.new(key, AES.MODE_CBC, iv)
padded = pad(mensaje, AES.block_size)  # Añadir padding al mensaje
cifrado = cipher.encrypt(padded)

print("Llave: ", key.hex())
print("IV: ", iv.hex())
print(f"Mensaje cifrado: {cifrado.hex()}")

# Descifrado
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
mensaje_descifrado_padded = cipher_dec.decrypt(cifrado)
mensaje_descifrado = unpad(mensaje_descifrado_padded, AES.block_size)

print(f"Mensaje descifrado: {mensaje_descifrado.decode('utf-8')}")