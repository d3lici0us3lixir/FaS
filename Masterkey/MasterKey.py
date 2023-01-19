import rekey, pskey, hashlib, hmac, json

def read_mascrypt(path):
    f = open(path+'\masterkey.cryptomator', 'r')
    data = json.load(f)
    mascryptlist = data
    f.close()
    return data['version'], data['scryptSalt'], data['scryptCostParam'], data['scryptBlockSize'], data['primaryMasterKey'], data['hmacMasterKey'], data['versionMac']

def let_hmac(version, in_key):
  sig =hmac.new(key = in_key, msg = version, digestmod=hashlib.sha256)
  sig = sig.digest()
  return sig

def make_recoverykey(input_recoverkey):
    recovery_key = []
    recovery_key = input_recoverkey.split(' ')
    return recovery_key




path = str(input('Enter the masterkey.cryptomator path ex)T:\crypto_test\\test_1011'))
version, scryptSalt, scryptCostParam, scryptBlockSize, primaryMasterKey, hmacMasterKey, versionMac  = read_mascrypt(path)
password = str(input('Input your password'))
ps_masterkey, ps_enkey, ps_mackey = pskey.password_masterkey(version, scryptSalt, scryptCostParam, scryptBlockSize, primaryMasterKey, hmacMasterKey, versionMac, password)

state = str(input('Do you have a recovery key? Y/N'))
if state == 'Y' or state == 'y':
    input_recoverkey = str(input('Enter your recovery key'))
    recovery_key = make_recoverykey(input_recoverkey)
    #re_nn : Get nn from recovery key
    re_masterkey, re_enckey, re_mackey = rekey.re_rekey(recovery_key)
    print('Masterkey from password     : ' + ps_masterkey.hex())
    print('Masterkey from recovery key : ' + re_masterkey.hex())
    print('Enckey from password        : ' + ps_enkey.hex())
    print('Enckey from recovery key    : ' + re_enckey.hex())
    print('Mackey from pssword         : ' + ps_mackey.hex())
    print('Mackey from recovery key    : ' + re_mackey.hex())

else:
    print('Program will shut down')
    print('Masterkey is :' + ps_masterkey.hex())
    print('Enckey is    :' + ps_enkey.hex())
    print('Mackey is    :' + ps_mackey.hex())
    