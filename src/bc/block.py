# -*- coding: utf-8 -*-

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
        self.hash = ""
        self.nonce = ""

