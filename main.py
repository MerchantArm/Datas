from Datas.core import db
from Datas.elements import *

MainBase = db.Datas("Test", "test")
print(MainBase.name)
print(MainBase.filename)
input()