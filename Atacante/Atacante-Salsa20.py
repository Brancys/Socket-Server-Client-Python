from Crypto.Cipher import Salsa20

key = input("Escriba la llave de cifrado: ")
nonce = input("Escriba el nonce del mensaje: ")
encrypted_message = input("Escriba el mensaje cifrado: ")


def decrypt(message, key, nonce):

    #Como recibimos la informacion en hex (por comodidad) la transformamos bytes
    key = bytes.fromhex(key)   
    nonce = bytes.fromhex(nonce)   
    message = bytes.fromhex(message)

    cipher = Salsa20.new(key=key, nonce=nonce)
    message = cipher.decrypt(message)
    print("[MENSAJE DESCIFRADO] ", message)

decrypt(encrypted_message, key, nonce)