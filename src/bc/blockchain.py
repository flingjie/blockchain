# -*- coding: utf-8 -*-
from .block import create_genesis_block, Block


class BlockChain:
    """
        区块链结构体
            blocks:        包含的区块列表
    """
    def __init__(self):
        self.blocks = [create_genesis_block()]

    def add_block(self, data):
        """
        添加区块
        :param block:
        :return:
        """
        prev_block = self.blocks[len(self.blocks)-1]
        self.blocks.append(Block(data, prev_block.hash))
