import hashlib
from operator import truediv
from unittest import result
# from cipher import *
from neatcipher import *

android_id = '78530472b1c87e18'
result1 = mix1(android_id)
result2 = mix2(result1)
result3 = mix3(result2)
userdbkey=hashlib.sha256(result3.encode()).hexdigest()
print('user.db key id: ', userdbkey)
# user.db key id:  60c9a124509894a70761e7417c8a6335e84e01e29b01e0bfe7878cea7fd658e3