from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from base64 import b64encode
from os import system
publicKey="""-----BEGIN PUBLIC KEY-----
            MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDR//qsgNjfQ0R8m6L9vglWKNvA
            0V/aCIonkK81JJolnadEbzX7FXe/7JL5CSoJNYn89vn3L74EzYCA1yHNej6cvIPv
            tZQ9OczBdp/tP/VrTCr3/89dP2FrJKh4QT04NGQ7Ed3GlzmGKzwCKeXrh2INeNSW
            BPDs+wCJeXy6bvnccwIDAQAB
            -----END PUBLIC KEY-----"""

if __name__=="__main__":
    message=input('输入需要加密的信息：')
    pbKey = RSA.importKey(str(publicKey))
    cipher = PKCS1_cipher.new(pbKey)
    rsa_text = b64encode(cipher.encrypt(bytes(message.encode("utf8"))))
    print('已保存为：密文.txt')
    print('加密后信息:')
    print(rsa_text.decode('utf-8'))
    with open('注册码.txt','w') as f:
        f.write(rsa_text.decode('utf-8'))
    system('pause')
