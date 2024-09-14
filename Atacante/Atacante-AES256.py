from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = input("Escriba la llave de cifrado: ")
iv = input("Escriba el iv del mensaje: ")
message = input("Escriba el mensaje cifrado: ")


def decrypt(key_hex, iv_hex, cifrado_hex):

    # Convertir hexadecimal a bytes
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)
    cifrado = bytes.fromhex(cifrado_hex)

    # Descifrado
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    mensaje_descifrado_padded = cipher_dec.decrypt(cifrado)
    mensaje_descifrado = unpad(mensaje_descifrado_padded, AES.block_size)

    print(f"Mensaje descifrado: {mensaje_descifrado.decode('utf-8')}")

decrypt(key, iv, message)