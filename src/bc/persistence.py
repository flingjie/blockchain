# -*- coding: utf-8 -*-
import pickle
import os


DB_NAME = 'data.pkl'


def save_data(data):
    with open(DB_NAME, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def load_data():
    data = None
    with open(DB_NAME, 'rb') as f:
        data = pickle.load(f)
    return data


def init_db():
    if not os.path.isfile(DB_NAME):
        save_data([])