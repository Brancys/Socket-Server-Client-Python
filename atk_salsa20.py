from Crypto.Cipher import Salsa20

def decrypt_salsa20(key, ciphertext, nonce):
    cipher = Salsa20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

#Llave, nonce y mensaje cifrado capturados con Wireshark
key = bytes.fromhex('31c9a6cb3f8bf5e9656da814314b6d40360e5b2347e88c098f6283daf35ce4dc')
nonce = bytes.fromhex('151d836a61945f5d')
msj = bytes.fromhex('9f97c895')

decrypting = decrypt_salsa20(key, msj, nonce)
print("Mensaje descrifrado: "+decrypting.decode('utf-8'))