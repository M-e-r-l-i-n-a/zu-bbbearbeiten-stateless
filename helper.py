from dataclasses import dataclass
import datetime

# Daten speichern
items = []


@dataclass
class Item:
    text: str
    date: datetime
    isCompleted: bool = False


# Ver-BBB-isierung
def add(text, date):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
    items.append(Item(text, date_object))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
