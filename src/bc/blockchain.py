# -*- coding: utf-8 -*-
from .block import Block
from .pow import ProofOfWork


def create_genesis_block():
    """
    生成创世区块,创世区块是第一个区块,故无父区块哈希
    :return:
    """
    block = Block(data="Genesis Block", prev_hash="")
    pow = ProofOfWork(block)
    nonce, digest = pow.mine()
    block.nonce = nonce
    block.hash = digest
    return block


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
        block = Block(data, prev_block.hash)
        pow = ProofOfWork(block)
        nonce, digest = pow.mine()
        block.nonce = nonce
        block.hash = digest
        self.blocks.append(block)
