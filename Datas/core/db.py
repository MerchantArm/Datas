import os
import sys

class Datas:
    def __init__(self, name, filename):
        assert filename != None, "Filename have status: None"
        self.name = name
        self.filename = filename