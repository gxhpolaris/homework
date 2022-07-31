from Cryptodome.Cipher import AES
from gmssl import sm2
import math
import random

mode=AES.MODE_OFB
iv=b'0000000000000011'
private_key='00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key='B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt=sm2.CryptSM2(public_key=public_key, private_key=private_key)

def encrypt_PGP(message,key):
    count=len(message)
    if (count%16==0):
        add=0
    else:
        add=16-(count%16)
    message=message+('\0'*add)
    mi=AES.new(key.encode('utf-8'),mode,iv)
    mi1=mi.encrypt(message.encode('utf-8'))
    plaintext=key.encode('utf-8')
    mi2=sm2_crypt.encrypt(plaintext)
    print("加密值为：",mi1)
    return mi1,mi2

def decrypt_PGP(mes1, mes2):
    mode=AES.MODE_OFB
    iv=b'0000000000000011'
    get_key=sm2_crypt.decrypt(mes2)
    mi=AES.new(get_key, mode, iv)
    plain_text=mi.decrypt(mes1)
    print("原消息值为：",plain_text.decode('utf-8'))

if __name__ == '__main__':
    mingwen="shandawangluokongjiananquan"
    print("消息为：",mingwen)
    key=hex(random.randint(2**127,2**128))[2:]
    result1,result2=encrypt_PGP(mingwen,key)
    decrypt_PGP(result1, result2)
