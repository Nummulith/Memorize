"""
Memorize!
Author: Pavel ERESKO
"""

import yaml

from ObjectModelFramework import *

class MemoItem(ObjectModelItem):
    Icon = "AWS"
    Color = "#e998ed"

    @classmethod
    def get_objects(cls, node = None):
        if node is None:
            return MemoObjectModel.DATA[cls.__name__]
        else:
            for obj in MemoItem.get_objects():
                if obj["Id"] == node:
                    return [obj]
            return []

    def get_icon(self):
        icon = super().get_icon()
        return os.path.abspath('./icons').replace("\\", "/") + "/" + icon + ".png"

class Service(MemoItem):
    Icon = "AWS"
    Color = "#adcdd9"
    Draw = DRAW.DEF - DRAW.CLASS - DRAW.ID


    @staticmethod
    def fields():
        return {
                    'Id'  : (Service, FIELD.ID),
                    'Name': (str, FIELD.VIEW),
                }

class Article(MemoItem):
    Icon = "AWS"
    Name = "Article"
    Color = '#84def4'
    Draw = DRAW.VIEW + DRAW.EXT

    @staticmethod
    def fields():
        return {
                    'Id'  : (Article, FIELD.ID),
                    'Name': (str, FIELD.VIEW),
                    'Links': ((Service,), FIELD.LINK),
                    'Note': (str, FIELD.EXT),
                }

class MemoObjectModel(ObjectModel):
    def __init__(self):
        super().__init__(
            "./src/Demo/Demo.xml",
            False,
            False,
            None,
            {
                'MEMO' : [
                    Article, Service, 
                ],
            }
        )

        with open(f'./data/Memo.yaml', 'r') as file:
            MemoObjectModel.DATA = yaml.safe_load(file)


OM = MemoObjectModel()
OM.fetch()

# OM.print()

# source = OM.source()
# with open('./data/Memo.svg', 'w') as file:
#     file.write(source)

draw = OM.html()
with open('./data/Memo.html', 'w') as file:
    file.write(draw)
