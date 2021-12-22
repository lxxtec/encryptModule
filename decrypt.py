import sys
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import base64
from argparse import ArgumentParser
import winreg
privateKey="""-----BEGIN RSA PRIVATE KEY-----
            MIICXAIBAAKBgQDR//qsgNjfQ0R8m6L9vglWKNvA0V/aCIonkK81JJolnadEbzX7
            FXe/7JL5CSoJNYn89vn3L74EzYCA1yHNej6cvIPvtZQ9OczBdp/tP/VrTCr3/89d
            P2FrJKh4QT04NGQ7Ed3GlzmGKzwCKeXrh2INeNSWBPDs+wCJeXy6bvnccwIDAQAB
            AoGAHIRBwpYWnS7RyIgL+KALPYd72/GyrfV16UyE9lb7lbsUYT8m2es+4TGbfbTo
            X+rEy7SwGgiCKb3MQvKz1ObSRJBBaFQdtu1kvzu1WWNpzRkvrUI3WP2Ak6YzH3UD
            IE7FBqNIHcMAchLebHnwBCHpb+yfC4yf79HKY15BXLLn+iECQQDUlb6zzs/dufoW
            YTEzxQB5NY6eGI6v/PRU0YHHwm5eZdax2oqHjk455rPy811EF5lTm2s2HvuFa/ws
            5ZuR8rnhAkEA/OMV4VYwap+vCp8nfoNGxEQO/Rpm6/kIzdUpEcbsAzQoY8m7FkO7
            XSz+sipYPjYxaEqUdZM09zxLWYrpLc+o0wJAXmY4jsPxjjY9lZ6HKMP8V9auhAnH
            ouKi5N870CbIt+ZlFglDprpMhm2pzuK+sbQBBB1p2FidvDudeZpkIMU2QQJANquB
            F23imapb1RgDGb6XleaAtwb2KR11YcorTsSKUUb9VFVQNMf/wWzwwuOUoB5nH/y/
            i4t/b9OBFqKJNnYmMQJBAJHHwbg+pIu1KmswAUwoezIf/VKAVY/5KoaI4y4y4pEe
            k5L2B7+48xZhfvVHCJyNyRxPuAS76CK3MLGLsL3Re1s=
            -----END RSA PRIVATE KEY-----"""

if __name__=='__main__':
    parser=ArgumentParser()
    parser.add_argument('--decode',type=str,default='')
    parser.parse_args()
    pri_key = RSA.importKey(privateKey)
    cipher = PKCS1_cipher.new(pri_key)
    back_text = cipher.decrypt(base64.b64decode(str(parser.decode)), 0)
    #print(back_text.decode('utf-8'))
    with open('info','w') as f:
        f.write(back_text.decode('utf-8'))