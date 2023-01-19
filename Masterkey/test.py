#Get masterkey from password
import base64
import scrypt
import awk
import hashlib
import hmac



def let_hmac(version,in_key):
  version = str(version)
  sig =hmac.new(key = in_key, msg = version, digestmod=hashlib.sha256)
  sig = sig.digest()
  print('Compute hmac with mackey' + sig)
  return sig



def password_masterkey(version, scryptSalt, scryptCostParam, scryptBlockSize, primaryMasterKey, hmacMasterKey, versionMac, password):
    salt = base64.b64decode(scryptSalt)
    primary = base64.b64decode(primaryMasterKey)
    hmackey = base64.b64decode(hmacMasterKey)
    kek = scrypt.hash(password, salt, scryptCostParam, scryptBlockSize, 1, 32)
    enckey = awk.aes_unwrap_key(kek, primary)
    mackey = awk.aes_unwrap_key(kek, hmackey)
    let_hmac(version, mackey)
    print('versionMac is ' + versionMac)
    return enckey+mackey, enckey, mackey
