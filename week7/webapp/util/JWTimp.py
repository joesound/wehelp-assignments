
import base64
import hmac
import hashlib 
import binascii
from datetime import datetime, timedelta
import random
import string
#convert utf-8 string to byte format
def toBytes(string):
	return bytes(string,'utf-8')

def encodeBase64(text):
	#remove "=" sign, 
	#P.S. "=" sign is used only as a complement in the final process of encoding a message. 
	return base64.urlsafe_b64encode(text).replace(b'=',b'')

#signature = HMAC-SHA256(key, unsignedToken)
def create_sha256_signature(key, unsignedToken):
	signature = hmac.new(toBytes(key), unsignedToken, hashlib.sha256).digest()
	return encodeBase64(signature)

def JWTencoder(header, payload, key):
    unsignedToken = encodeBase64(toBytes(header)) + toBytes('.') + encodeBase64(toBytes(payload))
    signature = create_sha256_signature(key,unsignedToken)
    jwt_toekn = unsignedToken.decode("utf-8") +'.'+signature.decode("utf-8")
    return jwt_toekn

def JWTdecoder(JWT):
    key = "fji234j;raewr823423"
    JWT_split = JWT.split(".")
    # for i in JWT_split:
    #     j = base64.b64decode(i)
    #     print(j)

def token_gen(user_data):
    unsignedToken = encodeBase64(toBytes(user_data))
    file1 = open('D:/sideproj/week5/webapp/util/Token_Gen.txt')
    key = file1.read()
    signature = create_sha256_signature(key,unsignedToken)
    file1.close()
    return signature.decode("utf-8")


def key_gen():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    print(ran_str)
    with open('D:/sideproj/week5/webapp/util/Token_Gen.txt', 'w') as f:
        f.write(ran_str)


# expire = datetime.utcnow() + timedelta(minutes=5)
# header	='{"alg":"HS256","typ":"JWT"}'
# payload = str({"user":"jamesshieh1111","timestamp":f"{expire}"})
# key 	= "fji234j;raewr823423"
# unsignedToken 	= encodeBase64(toBytes(header)) + toBytes('.') + encodeBase64(toBytes(payload))
# print(unsignedToken)
# signature 		= create_sha256_signature(key,unsignedToken)
# jwt_toekn = unsignedToken.decode("utf-8") +'.'+signature.decode("utf-8")
# print(jwt_toekn)
# token_deco = JWTdecoder(jwt_toekn)






