# -*- coding: utf-8 -*-
from .blockchain import BlockChain
from .persistence import init_db


def init_bc():
    """
    创建一个区块链
    :return:
    """
    init_db()

    bc = BlockChain()

    bc.add_block("Jack send 0.3 btc to Alice")
    bc.add_block("Alice send 0.1 btc to Tom")

    return bc