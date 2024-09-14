from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

# Cifrado
key = get_random_bytes(32)  # Salsa20 usa una llave de 256 bits (32 bytes)
nonce = get_random_bytes(8)  # El nonce es de 64 bits (8 bytes)
cipher = Salsa20.new(key=key, nonce=nonce)

mensaje = b"Tranquilo, los mensajes que enviamos por este medio son seguros porque los encriptamos todos."
cifrado = cipher.encrypt(mensaje)

print("Llave: ", key.hex())
print("Nonce: ", nonce.hex())
print(f"Mensaje cifrado: {cifrado.hex()}")