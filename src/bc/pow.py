# -*- coding: utf-8 -*-
import hashlib


class ProofOfWork():
    """
        工作量证明
    """
    def __init__(self, block, difficult=4):
        self.block = block
        self.difficulty = difficult

    def mine(self):
        """
            挖矿函数
        """
        i = 0
        prefix = '0' * self.difficulty

        while True:
            nonce = str(i)
            message = hashlib.sha256()
            message.update(str(self.block.prev_hash).encode('utf-8'))
            message.update(str(self.block.data).encode('utf-8'))
            message.update(str(self.block.timestamp).encode('utf-8'))
            message.update(nonce.encode("utf-8"))
            digest = message.hexdigest()
            if digest.startswith(prefix):
                return nonce, digest
            i += 1

    def validate(self):
        """
            验证有效性
        """
        message = hashlib.sha256()
        message.update(str(self.block.prev_hash).encode('utf-8'))
        message.update(str(self.block.data).encode('utf-8'))
        message.update(str(self.block.timestamp).encode('utf-8'))
        message.update(str(self.block.nonce).encode('utf-8'))
        digest = message.hexdigest()

        prefix = '0' * self.difficulty
        return digest.startswith(prefix)
