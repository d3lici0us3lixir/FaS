#Get Masterkey from recovery key
f = open('4096wordlist.txt', "r")

wordlist = []
while True:
    line = f.readline()
    if not line : break
    line = line.rstrip('\n')
    wordlist.append(line)
f.close()


def en_word(b1,b2,b3):
    t1 = (0xFF0 & (b1<<4)) + (0x00F &(b2>>4))
    t2 = (0xF00 & (b2 << 8)) + (0x0FF & b3)

    return t1,t2

def de_word(fw,sw):
    b1 = (0xFF & (fw >> 4))
    b2 = ((0xF0 & (fw << 4)) + (0x0F & (sw >> 8)))
    b3 = (0xFF & sw)
    return b1,b2,b3

#Get masterkey from recovery_key
def re_rekey(recovery_key):
    masterkey = bytearray([0]*66)
    for i in range(0, len(recovery_key),2):
        fw = wordlist.index(recovery_key[i])
        sw = wordlist.index(recovery_key[i+1])
        b1, b2, b3 = de_word(fw,sw)
        masterkey[i//2*3] = b1
        masterkey[i//2*3+1] = b2
        masterkey[i//2*3+2] = b3
    return masterkey[:64], masterkey[:32], masterkey[32:64]    

# Get recovery key from masterkey 
def make_rekey(masterkey):
    re_coverkey = bytearray([])
    for i in range(0, len(masterkey),3):
        b1 = masterkey[i]
        b2 = masterkey[i+1]
        b3 = masterkey[i+2]
        t1, t2 = en_word(b1,b2,b3)
        re_coverkey.append(wordlist[t1])
        re_coverkey.append(wordlist[t2])
    return re_coverkey