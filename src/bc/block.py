# -*- coding: utf-8 -*-

import hashlib
from datetime import datetime


class Block:
    """
        区块结构体
            prev_hash:      父区块哈希值
            data:           区块内容
            timestamp:      区块创建时间
            hash:           区块哈希值
    """
    def __init__(self, data, prev_hash):
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 计算区块的哈希值
        message = hashlib.sha256()
        message.update(str(self.prev_hash).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.timestamp).encode('utf-8'))
        self.hash = message.hexdigest()


def create_genesis_block():
    """
    生成创世区块,创世区块是第一个区块,故无父区块哈希
    :return:
    """
    return Block(data="Genesis Block", prev_hash="")
