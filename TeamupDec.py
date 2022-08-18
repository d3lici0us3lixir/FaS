from Crypto.Cipher import AES
import hashlib
import base64

def encode(text):
    block_size = 16
    text_length = len(text)
    amount_to_pad = block_size - (text_length % block_size)
    if amount_to_pad == 0:
        amount_to_pad = block_size
    pad = chr(amount_to_pad)
    return text + pad * amount_to_pad
    
android_id = '0b914a8be4013bcd'   
base = hashlib.sha256(bytes(android_id, 'utf-8')).hexdigest()
TMPkey = hashlib.sha256(bytes(base, 'utf-8')).hexdigest()
key =[]
for i in range(0, len(TMPkey),2):
    key.append(int('0x' + TMPkey[i:i+2], 16))
    tmp = i
key = bytes(key)
IV =  [0, 0, 0, 0,  0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0]
base = encode(base)

cipherAlg = AES.new(key, AES.MODE_CBC, bytes(IV))
Password = cipherAlg.encrypt(bytes(base, 'utf-8'))
print(base64.b64encode(Password).decode())
#https://jongmin86.tistory.com/207