# -*- coding: utf-8 -*-
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import binascii
import base58


class Wallet:
    """
        钱包
    """
    def __init__(self):
        random_gen = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random_gen)
        self.public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def address(self):
        """
            通过公钥生成地址
        """
        h = SHA.new(self.public_key.exportKey(format='DER'))
        return base58.b58encode(h.digest())

    def sign(self, message):
        """
            生成数字签名
        """
        h = SHA.new(message.encode('utf8'))
        return binascii.hexlify(self._signer.sign(h)).decode('ascii')


def verify_sign(pubkey, message, signature):
    """
        验证签名
    """
    verifier = PKCS1_v1_5.new(pubkey)
    h = SHA.new(message.encode('utf8'))
    return verifier.verify(h, binascii.unhexlify(signature))
